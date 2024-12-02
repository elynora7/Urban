import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        some_runner = Runner('Anna')
        for i in range(10):
            some_runner.walk()
        self.assertEqual(some_runner.distance, 50)

    def test_run(self):
        some_runner = Runner('Anna')
        for i in range(10):
            some_runner.run()
        self.assertEqual(some_runner.distance, 100)

    def test_challenge(self):
        some_runner1 = Runner('Anna')
        some_runner2 = Runner('Denis')
        for i in range(10):
            some_runner1.walk()
            some_runner2.run()
        self.assertNotEqual(some_runner1.distance, some_runner2.distance)



if __name__ == '__main__':
    unittest.main()