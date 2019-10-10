class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # DONE: Finish this initialization method. The file_name passed should be the full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        # DONE: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!

        f = open(self.file_name, 'w+')
        f.write(f"Population size: {pop_size}\tVaccination percentage: " +
                f"{vacc_percentage}\tVirus name: {virus_name}\t" +
                f"Mortality rate: {mortality_rate}\t" +
                f"Basic reproduction number: {basic_repro_num}\n")
        f.close()
        
        '''
        WITH allows you to open the file and automatically close the file without the close() method.
        It is the same as log_textfile = open('logfile.txt', 'w') then having to log_textfile.close() at the end.
        
        .writelines expects an iterable of strings from a list (log_content) and .write expects a single string
        '''


    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        f = open(self.file_name, 'a')
        if did_infect and not random_person_vacc and not random_person_sick:
            f.write(f"{person._id} infects {random_person._id}\n")
        elif not did_infect:
            if random_person_sick:
                f.write(f"{person._id} didn't infect {random_person._id} " +
                        "because they are already sick\n")
            elif random_person_vacc:
                f.write(f"{person._id} didn't infect {random_person._id} " +
                        "because they are already vaccinated\n")
        f.close()

    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.
        '''
        # DONE: Finish this method. If the person survives, did_die_from_infection should be False. Otherwise, did_die_from_infection should be True.

        with open(self.file_name, 'a') as log_textfile:
            #! Is did_die_from_infection supposed to be did_survive_infection? TODO: Fix later after confirmed.
            if person.did_die_from_infection() == False:
                log_textfile.write(f'{person.ID} survived infection.\n')
            else:
                log_textfile.write(f'{person.ID} died from infection\n')

    def log_time_step(self, time_step_number, infected_this_step,
                      died_this_time, cur_infected, total_dead):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        f = open(self.file_name, 'a')
        f.write("- - - - - - - - - - - - - - - - - - - - - \n")
        f.write(f"{infected_this_step} people were infected during TIME STEP "
                + f"{time_step_number}.\n")
        f.write(f"{died_this_time} people died during TIME STEP " +
                f"{time_step_number}.\n")
        f.write(f"{cur_infected} people are currently infected.\n")
        f.write(f"{total_dead} people died in total by far.\n")
        f.write(f"TIME STEP {time_step_number} ended, beginning TIME STEP " +
                f"{time_step_number + 1}.\n")
        f.write("- - - - - - - - - - - - - - - - - - - - - \n\n")
        f.close()
        # TODO: Finish this method. This method should log when a time step ends, and a new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass
