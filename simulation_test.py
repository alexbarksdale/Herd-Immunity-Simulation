import random
import sys
from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation
import pytest


def test_create_population():
    virus_name = Virus('SloppyBig', 0.15, 0.24)
    sim = Simulation(100, 0.30, virus_name, 1)

    infection_count = 0
    vaccinated_count = 0

    for person in sim.population:
        if person.infection:
            infection_count += 1
        else:
            vaccinated_count += 1

    assert infection_count == 1
    assert vaccinated_count == 99


def test_contructor():
    virus_name = Virus('SloppyBig', 0.15, 0.24)
    sim = Simulation(100, 0.30, virus_name, 1)
    assert sim.next_person_id == 100
    assert sim.total_infected == 1
    assert sim.vacc_percentage == .3
    assert sim.virus == virus_name
    assert sim.initial_infected == 1
    assert sim.total_dead == 0
    assert sim.file_name == "SloppyBig_simulation_pop_100_vp_0.3_infected_1.txt"
    assert sim.newly_infected == []


def test_infect_newly_infected():
    virus_name = Virus('Sloppy Big', 0.15, 0.24)
    sim = Simulation(100, 0.30, virus_name, 1)

    person = Person(1, True, None)
    rand_person = Person(2, False, infection=virus_name)

    sim.population.append(person)
    sim.population.append(rand_person)
    assert person.infection != virus_name
    assert rand_person.infection == virus_name
