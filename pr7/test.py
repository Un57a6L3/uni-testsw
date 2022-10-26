import unittest
from main import Mealy


class TestMealy(unittest.TestCase):
    def testStates1(self):
        o = Mealy()

        # Каждые две строки тестируют один вызов
        # Первая строка - возвращаемое значение
        # Вторая строка - состояние автомата
        self.assertEqual(o.sweep(), 0)
        self.assertEqual(o.getstate(), 'B')
        self.assertEqual(o.drag(), 3)
        self.assertEqual(o.getstate(), 'B')
        self.assertEqual(o.drag(), 3)
        self.assertEqual(o.getstate(), 'B')
        self.assertEqual(o.drag(), 3)
        self.assertEqual(o.getstate(), 'B')
        self.assertEqual(o.sweep(), 2)
        self.assertEqual(o.getstate(), 'C')
        self.assertRaises(KeyError, o.sweep)
        self.assertEqual(o.getstate(), 'C')
        self.assertEqual(o.make(), 5)
        self.assertEqual(o.getstate(), 'D')
        self.assertEqual(o.make(), 6)
        self.assertEqual(o.getstate(), 'E')
        self.assertEqual(o.sweep(), 7)
        self.assertEqual(o.getstate(), 'F')
        self.assertRaises(KeyError, o.sweep)
        self.assertEqual(o.getstate(), 'F')
        self.assertEqual(o.drag(), 8)
        self.assertEqual(o.getstate(), 'F')
        self.assertEqual(o.drag(), 8)
        self.assertEqual(o.getstate(), 'F')

    def testStates2(self):
        o = Mealy()

        # Каждые две строки тестируют один вызов
        # Первая строка - возвращаемое значение
        # Вторая строка - состояние автомата
        self.assertEqual(o.sweep(), 0)
        self.assertEqual(o.getstate(), 'B')
        self.assertEqual(o.drag(), 3)
        self.assertEqual(o.getstate(), 'B')
        self.assertEqual(o.sweep(), 2)
        self.assertEqual(o.getstate(), 'C')
        self.assertRaises(KeyError, o.sweep)
        self.assertEqual(o.getstate(), 'C')
        self.assertEqual(o.make(), 5)
        self.assertEqual(o.getstate(), 'D')
        self.assertEqual(o.make(), 6)
        self.assertEqual(o.getstate(), 'E')
        self.assertEqual(o.sweep(), 7)
        self.assertEqual(o.getstate(), 'F')
        self.assertEqual(o.drag(), 8)
        self.assertEqual(o.getstate(), 'F')
        self.assertEqual(o.drag(), 8)
        self.assertEqual(o.getstate(), 'F')
        self.assertRaises(KeyError, o.make)
        self.assertEqual(o.getstate(), 'F')
        self.assertEqual(o.drag(), 8)
        self.assertEqual(o.getstate(), 'F')
        self.assertEqual(o.drag(), 8)
        self.assertEqual(o.getstate(), 'F')
        self.assertEqual(o.drag(), 8)
        self.assertEqual(o.getstate(), 'F')


if __name__ == '__main__':
    unittest.main()
