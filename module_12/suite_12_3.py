import unittest
import tests_12_1
import tests_12_2

someST = unittest.TestSuite()
someST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
someST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

test_runner = unittest.TextTestRunner(verbosity=2)
test_runner.run(someST)
