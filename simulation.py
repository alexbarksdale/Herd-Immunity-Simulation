from virus import Virus
from logger import Logger
from person import Person
import random
import sys
random.seed(42)


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    #def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
    
    def __init__(self, pop_size, vacc_percentage, virus=None, initial_infected=1):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.

        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.

        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.

        You will need to keep track of the number of people currently infected with the disease.

        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.

        You will also need to keep track of the number of people that have die as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.logger = Logger(self.file_name)
        self.population = []  # List of Person objects
        self.pop_size = pop_size  # Int
        self.next_person_id = 0  # Int
        self.virus = virus  # Virus object
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0  # Int
        self.current_infected = 0  # Int
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, vacc_percentage, initial_infected, pop_size)
        self.newly_infected = []
        self.population = self._create_population()
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects. (return variable name: population)
        '''
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.
        population = []
        number_vaccinated = round(self.vacc_percentage * self.pop_size)
        total = random.sample(range(self.pop_size), number_vaccinated + self.initial_infected)
        infected = self.random_infected(total)
        vaccinated = total
        self.total_infected += self.initial_infected
        for item in range(self.pop_size):
            if item in vaccinated and item not in infected:
                population.insert(item, Person(item, True))
            elif item not in vaccinated and item in infected:
                population.insert(item, Person(item, False, self.virus))
            else:
                population.insert(item, Person(item, False))

        return population

    def find_dead(self):
        """ Finds all the dead people"""
        dead = 0 
        for person in self.population:
            if person != person.is_alive:
                dead += 1
        return dead


    def get_none(self):
        ''' Returns all the alive people who are not vaccinated or infected: normal people'''
        normal = 0
        alive = self.get_alive()
        for person in alive:
            if person != person.infection and person != person.is_vaccinated:
                normal += 1
        return normal

    def get_alive_num(self):
        """Return the number of alive people in the population."""
        alive_num = 0
        for person in self.population:
            if person.is_alive:
                alive_num += 1
        return alive_num


    def get_alive(self, id=-1):
        """ helper function that returns a list of alive people """
        alive = []
        for person in self.population:
            if person.is_alive and not person._id == id:
                alive.append(person)
        return alive


    def get_infected(self):
        ''' Helper function that gets all alive infected people in population'''
        alive_sick = []
        for person in self.population:
            if person.infected and person.is_alive:
                alive_sick.append(person)
        return alive_sick


    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.
            Returns:
                bool: False for simulation should continue, True otherwise.
        '''
        # find the number of people who are both alive and vaccinated
        alive_vacc = 0
        for person in self.population:
            if person.is_alive and person.is_vaccinated:
                alive_vacc += 1
        # make decision
        return self.total_dead + alive_vacc >= self.pop_size

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.
        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 1
        simulation_should_continue = 0
        should_continue = None

        while True:
            self.time_step(time_step_counter)
            # create a list of alive persons
            alive = self.get_alive()
            # create a list of vaccinated persons
            vaccinated = []
            for person in self.population:
                if person in alive and person.is_vaccinated:
                    vaccinated.append(person)
            # create a list of uninfected persons
            uninfected = []
            for person in alive:
                if person not in vaccinated and person.infection:
                    uninfected.append(person)
            print(f"Time step: {time_step_counter}, " +
                  f"total infected: {self.total_infected}, " +
                  f"current infected: {self.current_infected} vaccinated %: " +
                  f"{self.vacc_percentage}, dead: {self.total_dead},  " +
                  f"total vaccinated: {len(vaccinated)}, " +
                  f"alive: {len(alive)}, uninfected: {len(uninfected)}")

            if self._simulation_should_continue():
                simulation_should_continue += 1
                break

            time_step_counter += 1
        print(f'The simulation has ended after {time_step_counter} turns.')

    def time_step(self, time_step_counter):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''

        dead_this_time = 0
        for person in self.population:
            if person.infection and person.is_alive:
                sample = random.sample(self.get_alive(person._id), 100)
                interaction_sample = sample
                for random_person in interaction_sample:
                    self.interaction(person, random_person)
                did_survive = person.did_survive_infection()
                self.logger.log_infection_survival(person, did_survive)
                if not did_survive:
                    dead_this_time += 1
                    self.total_dead += 1
                self.current_infected -= 1
        infected_this_step = self._infect_newly_infected()
        self.logger.log_time_step(time_step_counter, infected_this_step, dead_this_time, self.total_infected, self.total_dead)



    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        if random_person == person.is_vaccinated:
            self.logger.log_interaction(person, random_person, random_person_vacc=True)
        elif random_person.infection:
            self.logger.log_interaction(person, random_person, random_person_sick=True)
        elif (random_person.infection is None and not random_person.is_vaccinated):
            num = random.random()
            if num < self.virus.repro_rate:
                random_person.infection = self.virus
                self.newly_infected.append(random_person._id)
                self.total_infected += 1
                self.current_infected += 1
                self.logger.log_interaction(person, random_person,did_infect=True)        
        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
        # random_person is vaccinated:
        #     nothing happens to random person.
        # random_person is already infected:
        #     nothing happens to random person.
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0 and 1.  If that number is smaller
        #     than repro_rate, random_person's ID should be appended to
        #     Simulation object's newly_infected array, so that their .infected
        #     attribute can be changed to True at the end of the time step.

        # TODO: Calls logger method during this method.

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        num_infected = 0
        for people in self.newly_infected:
            self.population[people].infection = self.virus
            num_infected += 1
        self.newly_infected = []
        return num_infected 


        


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
