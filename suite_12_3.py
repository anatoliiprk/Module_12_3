import unittest
import tests_12_3

print('------\nЗадача "Заморозка кейсов"\n------')

runST = unittest.TestSuite()
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

launch = unittest.TextTestRunner(verbosity=2)
launch.run(runST)