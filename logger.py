class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''

    def __init__(self, file_name):
        self.file_name = file_name

    '''
    The simulation class should use this method immediately to log the specific
    parameters of the simulation as the first line of the file.
    '''

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        WITH allows you to open the file and automatically close the file without the close() method.
        It is the same as log_textfile = open('logfile.txt', 'w') then having to log_textfile.close() at the end.
        .writelines expects an iterable of strings from a list (log_content) and .write expects a single string
        '''
        with open(self.file_name, 'w') as log_textfile:
            log_textfile.write(f"Population size: {pop_size}\tVaccination percentage: " +
                               f"{vacc_percentage}\tVirus name: {virus_name}\t" +
                               f"Mortality rate: {mortality_rate}\t" +
                               f"Basic reproduction number: {basic_repro_num}\n")

    '''
    The Simulation object should use this method to log every interaction
    a sick person has during each time step.
    The format of the log should be: "{person.ID} infects {random_person.ID} \n"
    or the other edge cases:
        "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
    '''

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):

        with open(self.file_name, 'a') as log_textfile:
            if did_infect and not random_person_vacc and not random_person_sick:
                log_textfile.write(
                    f'{random_person._id} got infected by {person._id}.\n')
            elif not did_infect:
                if random_person_sick:
                    log_textfile.write(
                        f'{random_person._id} and {person._id} were already sick, can\'t infect the already infected!\n')
                elif random_person_vacc:
                    log_textfile.write(
                        f'{random_person._id} couldn\'t infect {person._id} because they are vaccinated!\n')

    ''' 
    The Simulation object uses this method to log the results of every
    call of a Person object's .resolve_infection() method.
    '''

    def log_infection_survival(self, person, did_die_from_infection):
        with open(self.file_name, 'a') as log_textfile:
            if did_die_from_infection:
                log_textfile.write(f"{person._id} died from infection.\n")
            elif not did_die_from_infection:
                log_textfile.write(f"{person._id} survived infection.\n")

    def log_time_step(self, time_step_number, infected_this_step,
                      died_this_time, cur_infected, total_dead):
        with open(self.file_name, 'a') as log_textfile:
            stats = f'{infected_this_step} people were infected during TIME STEP {time_step_number}.\n' + f'{died_this_time} people died during TIME STEP {time_step_number}.\n' + \
                f'{cur_infected} people are currently infected.\n {total_dead} people died in total by far.\n' + \
                    f'TIME STEP {time_step_number} ended, beginning TIME STEP {time_step_number + 1}.'

            divider = '-' * 40
            log_textfile.write(divider + '\n')
            log_textfile.write(stats)
            log_textfile.write('\n' + divider)
