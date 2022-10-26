# Класс реализует модель автомата Мили
# (Конечный автомат, выходные значения которого
# определяются входными значениями и состоянием)
class Mealy:
    # Начальное состояние - A
    def __init__(self):
        self.__state = 'A'

    # Свойство, возвращающее состояние
    def getstate(self):
        return self.__state

    # Один из методов, изменяющих состояние
    def sweep(self):
        if self.__state == 'A':
            self.__state = 'B'
            return 0
        if self.__state == 'B':
            self.__state = 'C'
            return 2
        if self.__state == 'E':
            self.__state = 'F'
            return 7
        raise KeyError

    # Один из методов, изменяющих состояние
    def drag(self):
        if self.__state == 'B':
            return 3
        if self.__state == 'F':
            return 8
        raise KeyError

    # Один из методов, изменяющих состояние
    def make(self):
        if self.__state == 'A':
            self.__state = 'E'
            return 1
        if self.__state == 'B':
            self.__state = 'F'
            return 4
        if self.__state == 'C':
            self.__state = 'D'
            return 5
        if self.__state == 'D':
            self.__state = 'E'
            return 6
        raise KeyError


if __name__ == '__main__':
    o = Mealy()
    actions = [
        'sweep',
        'drag',
        'drag',
        'drag',
        'sweep',
        'drag',
        'make',
        'make',
        'sweep',
        'sweep',
        'drag',
        'drag'
    ]

    for action in actions:
        try:
            print(getattr(o, action)())
        except KeyError as e:
            print('KeyError')
        except:
            print('Other Error')
        # finally:
        #     print(o.getstate())
