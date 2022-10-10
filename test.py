import unittest
from main import Matrix


class TestMatrix(unittest.TestCase):
    def testAdd(self):
        m1 = Matrix.fill(2, 3, 1)
        m2 = Matrix.fill(2, 2, -1)
        m3 = Matrix.fill(2, 2, 1)
        m4 = Matrix([[2, 4, 3], [5, 1, 2]])
        m5 = Matrix.identity(3)
        m6 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m7 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        m8 = Matrix.fill(3, 3, 1)
        self.assertEqual(Matrix.add(m1, m1).data, [[2, 2, 2], [2, 2, 2]])
        self.assertEqual(Matrix.add(m2, m3).data, [[0, 0], [0, 0]])
        self.assertEqual(Matrix.add(m4, m5).data, "IndexError")
        self.assertEqual(Matrix.add(m6, m7).data, [[10, 10, 10], [10, 10, 10],
                                                   [10, 10, 10]])
        self.assertEqual(Matrix.add(m7, m8).data, [[10, 9, 8], [7, 6, 5],
                                                   [4, 3, 2]])

    # TODO
    def testSub(self):
        m1 = Matrix.fill(2, 3, 1)
        m2 = Matrix.fill(2, 2, -1)
        m3 = Matrix.fill(2, 2, 1)
        m4 = Matrix([[2, 4, 3], [5, 1, 2]])
        m5 = Matrix.identity(3)
        m6 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        m7 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
        m8 = Matrix.fill(3, 3, 1)
        self.assertEqual(Matrix.sub(m1, m1).data, [[0, 0, 0], [0, 0, 0]])
        self.assertEqual(Matrix.sub(m3, m2).data, [[2, 2], [2, 2]])
        self.assertEqual(Matrix.sub(m4, m5).data, "IndexError")
        self.assertEqual(Matrix.sub(m6, m7).data, [[-8, -6, -4], [-2, 0, 2],
                                                   [4, 6, 8]])
        self.assertEqual(Matrix.sub(m7, m8).data, [[8, 7, 6], [5, 4, 3],
                                                   [2, 1, 0]])

    def testMul(self):
        m1 = Matrix.fill(2, 3, -1)
        m2 = Matrix.fill(3, 2, -1)
        m3 = Matrix.fill(3, 3, 5)
        m4 = Matrix.identity(3)
        self.assertEqual(Matrix.mul(m1, m2).data, [[3, 3], [3, 3]])
        self.assertEqual(Matrix.mul(m1, m1).data, 'IndexError')
        self.assertEqual(Matrix.mul(m3, m4).data, [[5, 5, 5], [5, 5, 5],
                                                   [5, 5, 5]])
        self.assertEqual(Matrix.mul(m1, 2).data, [[-2, -2, -2], [-2, -2, -2]])
        self.assertEqual(Matrix.mul(m4, [1, 2, 3]).data, 'TypeError')

    def testPow(self):
        m1 = Matrix.fill(3, 3, -1)
        m2 = Matrix.fill(3, 3, 0)
        m3 = Matrix.fill(3, 2, 5)
        m4 = Matrix.fill(3, 3, 2)
        self.assertEqual(Matrix.pow(m1, 2).data, [[3, 3, 3], [3, 3, 3],
                                                  [3, 3, 3]])
        self.assertEqual(Matrix.pow(m3, 3).data, 'IndexError')
        self.assertEqual(Matrix.pow(m2, 2).data, [[0, 0, 0], [0, 0, 0],
                                                  [0, 0, 0]])
        self.assertEqual(Matrix.pow(m1, 3).data, [[-9, -9, -9], [-9, -9, -9],
                                                  [-9, -9, -9]])
        self.assertEqual(Matrix.pow(m4, 8).data, [[559872, 559872, 559872],
                                                  [559872, 559872, 559872],
                                                  [559872, 559872, 559872]])

    # TODO
    def testTranspose(self):
        pass


if __name__ == "__main__":
    unittest.main()
