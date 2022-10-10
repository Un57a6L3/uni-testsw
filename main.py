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
    # TODO
    def mul():
        pass

    # Метод возведения матрицы в степень
    # TODO
    def pow():
        pass

    # Единичная матрица заданного размера
    # TODO
    def identity():
        pass

    # Метод транспонирования матрицы
    # TODO
    def transpose():
        pass

    # Метод для пользовательского ввода
    # TODO
    def enter():
        pass


# TODO
def main():
    pass


if __name__ == "__main__":
    main()
