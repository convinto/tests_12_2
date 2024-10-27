class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

#-----------------------------------------------------------------------------------------------------------------------

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):        #производится перед каждым тестированием
        self.runer1 = Runner('Усэйн', 10)
        self.runer2 = Runner('Андрей', 9)
        self.runer3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results.values():
            print_result = {}
            for key, value in i.items():
                print_result[key] = value.name
            print(print_result)

    def test_run1(self):
        self.sprint1 = Tournament(90, self.runer1, self.runer3)
        self.all_results = self.sprint1.start()
        max_place_sprint = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(max_place_sprint == 'Ник')

        TournamentTest.all_results[1] = self.all_results

    def test_run2(self):
        self.sprint2 = Tournament(90, self.runer2, self.runer3)
        self.all_results = self.sprint2.start()
        max_place_sprint = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(max_place_sprint == 'Ник')

        TournamentTest.all_results[2] = self.all_results

    def test_run3(self):
        self.sprint3 = Tournament(90, self.runer1, self.runer2, self.runer3)
        self.all_results = self.sprint3.start()
        max_place_sprint = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(max_place_sprint == 'Ник')

        TournamentTest.all_results[3] = self.all_results

if __name__ == '__main__':
    unittest.main()