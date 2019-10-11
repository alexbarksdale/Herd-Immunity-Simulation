# Final Project: Herd Immunity Simulation

A  program that runs a basic simulation of herd immunity by modeling how a virus moves through a population where some (but not all) of a population is vaccinated against this virus.

## Authors

* **Alex Barksdale and Andre Williams** - [Andre's GitHub](https://github.com/Andre-Williams22)

### Rules

1. A sick person only has a chance at infecting healthy, unvaccinated people they encounter.  
1. An infected person cannot infect a vaccinated person.  This still counts as an interaction.  
1. An infected person cannot infect someone that is already infected.  This still counts as an interaction.
1. At the end of a time step, an infected person will either die of the infection or get better.  The chance they will die is the percentage chance stored in mortality_rate.  
1. For simplicity's sake, if the person does not die, we will consider them immune to the virus and change is_vaccinated to True when this happens.  
1. Dead people can no longer be infected, either.  Any time an individual dies, we should also change their .infected attribute to False.  
1. All state changes for a person should occur at the **end** of a time step, after all infected persons have finished all of their interactions.  
1. During the interactions, make note of any new individuals infected on this turn.  After the interactions are over, we will change the .infected attribute of all newly infected individuals to True.  1. Resolve the states of all individuals that started the turn infected by determining if they die or survive the infection, and change the appropriate attributes.  
1. The simulation should output a logfile that contains a record of every interaction that occurred during the simulation.  We will use this logfile to determine final statistics and answer questions about the simulation.

## Getting Started

**Important:**
Please follow these instructions *exactly*. 

### Installing

1. Clone the respository
```
git clone https://github.com/alexbarksdale/Herd-Immunity-Simulation.git
```
2. Make sure you're in the correct directory

3. The program is designed to be run from the command line:
```
python3  simulation.py (POPULATION SIZE) (VACC PERCENTAGE) (VIRUS NAME) (INITIAL INFECTED)
```
 Let's look at an example:
 * Population Size: 100,000
 * Vaccination Percentage: 90%
 * Virus Name: Ebola
 * Mortality Rate: 70%
 * Reproduction Rate: 25%
 * People Initially Infected: 10

The example input would be: <br>
 `python3 simulation.py 100000 0.90 Ebola 0.70 0.25 10` in the terminal.
 
 ## Acknowledgments

* Used Make School's starter code to get started: [Make School's Repo](https://github.com/Make-School-Labs/Herd-Immunity-Simulation)
