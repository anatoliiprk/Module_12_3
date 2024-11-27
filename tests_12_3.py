from pprint import pprint
import unittest


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
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)
        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        first = Runner('first runner')
        i = 10
        while i:
            first.walk()
            i -= 1
        self.assertEqual(first.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        second = Runner('second runner')
        i = 10
        while i:
            second.run()
            i -= 1
        self.assertEqual(second.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        third = Runner('third runner')
        fourth = Runner('fourth runner')
        i = 10
        while i:
            third.run()
            fourth.walk()
            i -= 1
        self.assertNotEqual(third.distance, fourth.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.run1 = Runner('Усейн', 10)
        self.run2 = Runner('Андрей', 9)
        self.run3 = Runner('Ник', 3)

    @classmethod
    def tearDown(cls):
        pprint(cls.all_results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        tournam1 = Tournament(90, self.run1, self.run3)
        result_1 = tournam1.start()
        self.all_results.update(result_1)
        self.assertTrue(self.all_results[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        tournam2 = Tournament(90, self.run2, self.run3)
        result_2 = tournam2.start()
        self.all_results.update(result_2)
        self.assertTrue(self.all_results[2], 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        tournam3 = Tournament(90, self.run1, self.run2, self.run3)
        result_3 = tournam3.start()
        self.all_results.update(result_3)
        self.assertTrue(self.all_results[3], 'Ник')




if __name__ == '__main__':
    unittest.main