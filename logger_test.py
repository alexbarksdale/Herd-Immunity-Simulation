from person import Person
from logger import Logger
import os
import pytest


def test_log_interaction():
    file_name = Logger('test.txt')

    person = Person(1, True)
    random_person = Person(2, False)

    file_name.log_interaction(person, random_person, False, True, False)

    with open('test.txt', 'r') as text_log:
        test = text_log.read()

    assert "2 couldn't infect 1 because they are vaccinated!" in test
    os.remove('test.txt')


def test_log_infection_survival():
    file_name = Logger('test.txt')

    person = Person(1, True)
    file_name.log_infection_survival(person, True)

    with open('test.txt', 'r') as text_log:

        test = text_log.read()

        assert '1 died from infection.\n' in test
    os.remove('test.txt')


def test_write_metadata():
    file_name = Logger('test.txt')
    file_name.write_metadata(50, 0.3, 'Ebola', 0.3, 0.3)

    with open('test.txt', 'r') as text_log:
        test = text_log.read()
        assert test == 'Population size: 50	Vaccination percentage: 0.3	Virus name: Ebola	Mortality rate: 0.3	Basic reproduction number: 0.3\n'
    os.remove('test.txt')
