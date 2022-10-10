class Matrix:
    # Инициализация матрицы из вложенного списка
    def __init__(self, data):
        self.data = data
        self.mdim = len(data)
        self.ndim = len(data[0])

    # Создание матрицы, заполненной заданным числом
    @staticmethod
    def fill(mdim, ndim, value=1):
        return Matrix([[value] * ndim for _ in range(mdim)])

    # Вывод матрицы
    def print(self):
        for num in self.data:
            print('\t'.join(map(str, num)))

    # Метод сложения двух матриц
    @staticmethod
    def add(op1: 'Matrix', op2: 'Matrix'):
        # Проверка, совпадают ли размеры матриц
        if op1.ndim != op2.ndim or op1.mdim != op2.mdim:
            return type('obj', (object,), {'data': 'IndexError'})

        # Сложение матриц
        res = Matrix.fill(op1.mdim, op1.ndim)
        for m in range(res.mdim):
            for n in range(res.ndim):
                res.data[m][n] = op1.data[m][n] + op2.data[m][n]
        return res

    # Метод вычитания двух матриц
    # TODO
    def sub(op1: 'Matrix', op2: 'Matrix'):
        # Проверка, совпадают ли размеры матриц
        if op1.ndim != op2.ndim or op1.mdim != op2.mdim:
            return type('obj', (object,), {'data': 'IndexError'})

        # Вычитание матриц
        res = Matrix.fill(op1.mdim, op1.ndim)
        for m in range(res.mdim):
            for n in range(res.ndim):
                res.data[m][n] = op1.data[m][n] - op2.data[m][n]
        return res

    # Метод умножения двух матриц (или матрицы и числа)
    @staticmethod
    def mul(op1: 'Matrix', op2):
    # Проверка типа, умножение на число
        if type(op2) in (int, float):
            res = Matrix.fill(op1.mdim, op1.ndim)
            for m in range(op1.mdim):
                for n in range(op1.ndim):
                    res.data[m][n] = op1.data[m][n] * op2
            return res

        # Проверка типа и длин нужных сторон матриц
        if type(op2) is not Matrix:
            return type('obj', (object,), {'data': 'TypeError'})
        if op1.ndim != op2.mdim:
            return type('obj', (object,), {'data': 'IndexError'})

        # Умножение матриц
        res = Matrix.fill(op1.mdim, op2.ndim, value=0)
        for m in range(op1.mdim):
            for n in range(op2.ndim):
                for i in range(op1.ndim):
                    res.data[m][n] += op1.data[m][i] * op2.data[i][n]
        return res

    # Метод возведения матрицы в степень
    @staticmethod
    def pow(op1: 'Matrix', op2: int):
        if op1.mdim != op1.ndim:
            return type('obj', (object,), {'data': 'IndexError'})
        res = Matrix.identity(op1.mdim)
        for _ in range(op2):
            res = Matrix.mul(res, op1)
        return res

    # Единичная матрица заданного размера
    @staticmethod
    def identity(dim: int):
        res = Matrix.fill(dim, dim, value=0)
        for i in range(dim):
            res.data[i][i] = 1
        return res
    """
    # Метод транспонирования матрицы
    # TODO
    def transpose():
        pass

    # Метод для пользовательского ввода
    # TODO
    def enter():
        pass
    """

# TODO
def main():
    pass


if __name__ == "__main__":
    main()
