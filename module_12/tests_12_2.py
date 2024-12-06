import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.results = []

    @classmethod
    def tearDownClass(cls):
        print('\n'.join(cls.results))

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    def tearDown(self):
        some_dict = {}
        for key, value in self.all_results.items():
            some_dict[key] = str(value)
        self.results.append(str(some_dict))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tournament = Tournament(90, self.runner_1, self.runner_3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[2] == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tournament = Tournament(90, self.runner_2, self.runner_3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[2] == self.runner_3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tournament = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[3] == self.runner_3)



if __name__ == '__main__':
    unittest.main()