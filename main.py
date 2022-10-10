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
    @staticmethod
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

    # Метод транспонирования матрицы
    @staticmethod
    def transpose(op: 'Matrix'):
        res = Matrix.fill(op.ndim, op.mdim)
        for m in range(op.mdim):
            for n in range(op.ndim):
                res.data[n][m] = op.data[m][n]
        return res

    # Метод для пользовательского ввода
    @staticmethod
    def enter():
        temp = input('Введите размер матрицы (строки и столбцы): ')
        matrix = []
        row = None
        isfloat = False
        mdim, ndim = list(map(int, temp.split()))
        print(f'Введите матрицу построчно через пробел')
        m = 0
        while m < mdim:
            temp = input().split()
            try:
                if isfloat is True:
                    raise ValueError
                row = list(map(int, temp))
            except ValueError:
                try:
                    row = list(map(float, temp))
                    isfloat = True
                except:
                    print('Неверный ввод')
                    return
            if len(row) == ndim:
                matrix.append(row)
                m += 1
            else:
                print('Неверное кол-во эл-тов в строке')
        return Matrix(matrix)


def main():
    matrices = {}  # Пустой словарь, будет заполняться пользователем
    actions = {
        # Номер действия: (текст, вызываемый метод, кол-во матриц, кол-во чисел)
        1: ('Ввод матрицы', Matrix.enter, 0, 0),
        2: ('Сложение матриц', Matrix.add, 2, 0),
        3: ('Вычитание матриц', Matrix.sub, 2, 0),
        4: ('Умножение матрицы на число', Matrix.mul, 1, 1),
        5: ('Умножение матриц', Matrix.mul, 2, 0),
        6: ('Возведение матрицы в степень', Matrix.pow, 1, 1),
        7: ('Транспонирование матрицы', Matrix.transpose, 1, 0),
        0: ('Завершить работу',)
    }
    # Внешний цикл
    onflag = True
    print('--- Перед действиями задайте матрицы, над которыми действие выполняется ---')
    while onflag:
        print('\nВыберите действие из списка')
        for key, value in actions.items():
            print(f'{key}: {value[0]}')
        action = int(input('Введите номер действия: '))
        args = []

        # Выход из цикла
        if action == 0:
            onflag = False
            break
        # Действия
        if len(matrices) < actions[action][2]:
            print('Перед действием введите матрицы над которыми оно производится')
            continue
        for i in range(actions[action][2]):
            temp = input(f'Введите имя матрицы {i + 1}: ')
            args.append(matrices[temp])
        for i in range(actions[action][3]):
            temp = float(input(f'Введите число: '))
            if temp.is_integer():
                temp = int(temp)
            args.append(temp)
        res = actions[action][1](*args)
        temp = chr(ord('A') + len(matrices))
        matrices[temp] = res
        if action != 1:
            print('Результат:')
            matrices[temp].print()
        print(f'Матрица записана под именем {temp}')


if __name__ == "__main__":
    main()
