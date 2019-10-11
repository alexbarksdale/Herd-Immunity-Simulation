import unittest


class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        err_msg = "Rates are too high!"
        assert repro_rate <= 1 or mortality_rate <= 1, err_msg
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


class TestVirus(unittest.TestCase):
    '''Check to make sure that the virus instantiator is working.'''

    def test_virus_instantiation(self):
        virus = Virus("HIV", 0.8, 0.3)
        assert virus.name == "HIV"
        assert virus.repro_rate == 0.8
        assert virus.mortality_rate == 0.3

        ebola = Virus('ebola', .6, .5)
        assert ebola.name == "ebola"
        assert ebola.repro_rate == .6
        assert ebola.mortality_rate == .5

        Mumps = Virus('Mumps', .2, .7)
        assert Mumps.name == "Mumps"
        assert Mumps.repro_rate == .2
        assert Mumps.mortality_rate == .7

        HIV = Virus('HIV', .8, .8)
        assert HIV.name == 'HIV'
        assert HIV.repro_rate == .8
        assert HIV.mortality_rate == .8

        malaria = Virus('Malaria', .4, .2)
        assert malaria.name == 'malaria'
        assert malaria.repro_rate == .4
        assert malaria.mortality_rate == .2

    '''
    Credit to
    https://stackoverflow.com/questions/88325/how-do-i-unit-test-an-init-method-of-a-python-class-with-assertraises
    for inspiring this test.
    '''

    def test_insufficient_args(self):
        name = "HIV"
        repro_rate = 1.2
        mortality_rate = 2.9
        self.assertRaises(AssertionError,
                          Virus, name, repro_rate, mortality_rate)


if __name__ == '__main__':
    unittest.main()
