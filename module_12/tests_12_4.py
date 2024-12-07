import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            some_runner = Runner('Anna')
            some_runner2 = Runner('Вася', -5)
            for i in range(10):
                some_runner.walk()
                some_runner2.walk()
            self.assertEqual(some_runner.distance, 50)
            self.assertEqual(some_runner2.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            some_runner = Runner('Anna')
            some_runner2 = Runner(2)
            for i in range(10):
                some_runner.run()
                some_runner2.run()
            self.assertEqual(some_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner', exc_info=True)
        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        some_runner1 = Runner('Anna')
        some_runner2 = Runner('Denis')
        for i in range(10):
            some_runner1.walk()
            some_runner2.run()
        self.assertNotEqual(some_runner1.distance, some_runner2.distance)

if __name__ == '__main__':
    unittest.main()
