from random import uniform
from virus import Virus


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = None  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = None  # boolean
        self.infection = None  # Virus object or None

    def did_survive_infection(self):
        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        '''
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean
        # while self.infection != None:
        #     num = random.uniform(0, 1)
        #     if num <= self.infection.mortality_rate:
        #         return False
        #     else:
        #         return True
        if self.infection:
            num = uniform(0, 1)
            if num <= self.infection.mortality_rate:
                # this person died
                self.is_alive = False
                return False
            else:
                # this person survives
                self.is_vaccinated = True
                return True


''' These are simple tests to ensure that you are instantiating your Person class correctly. '''
def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    dani = Person(4, True, None)
    assert dani._id == 4, "it's not 4"
    assert dani.is_alive == True, "It's not true"
    assert dani.is_vaccinated == True
    assert dani.infection == None

    michelle = Person(3, True, None)
    assert michelle._id == 3
    assert michelle.is_alive == True
    assert michelle.is_vaccinated == True
    assert michelle.infection == None

    dan = Person(6, True, None)
    assert dan._id == 6 
    assert dan.is_alive == True
    assert dan.is_vaccinated == True
    assert dan.infection == None

    jess = Person(1, True, None)
    assert jess._id == 1
    assert jess.is_alive == True
    assert jess.is_vaccinated == True
    assert jess.infection == None

    


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    assert person._id == 2
    assert person.is_alive == False
    


def test_sick_person_instantiation():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(3, True, virus)
    # TODO: complete your own assert statements that test
    # the values at each attribute
    # assert ...
    assert person._id == 3
    assert person.is_alive == True
    assert person.is_vaccinated == False
    assert person.infection == virus
    


def test_did_survive_infection():
    # TODO: Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # TODO: Create a Person object and give them the virus infection
    person = Person(4, False, virus)

    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
        assert person.is_alive is True
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who survived
        # assert ...
        assert person.is_vaccinated == True
    else:
        assert person.is_alive is False
        # TODO: Write your own assert statements that test
        # the values of each attribute for a Person who did not survive
        # assert ...
        assert person.is_vaccinated == False
        
