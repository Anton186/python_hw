class Matrix:
    _matrix: list[list[int | float]] = None
    _rows: int = None
    _clmns: int = None

    def __init__(self, matrix: list[list[int | float]]) -> None:
        """
        :param matrix: [[int | float]]  -> матрица размерностью rows X clmns
        :param rows: int                -> a number of rows
        :param clmns: int               -> a number of columns
        """
        self._matrix = matrix
        self._rows = len(matrix)
        self._clmns = len(matrix[0])

    @property
    def rows(self):
        return self._rows

    @property
    def clmns(self):
        return self._clmns

    def __repr__(self):
        return f'Matrix({self._matrix})'

    def _eq_len(self, other):
        return self._rows == other._rows and \
               self._clmns == other._clmns

    def __eq__(self, other):
        flag = True
        if self is other:
            logger.info(f'СРАВНЕНИЕ: {self._matrix} = {other._matrix}')
            return flag
        else:
            for i in range(self._rows):
                for j in range(self._clmns):
                    if self._matrix[i][j] != other._matrix[i][j]:
                        flag = False
                        logger.info(f'СРАВНЕНИЕ: {self._matrix} != {other._matrix}')
                        break
        return flag

    def __add__(self, other):
        new_mtrx = [[0 for j in range(self._clmns)] for i in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._clmns):
                new_mtrx[i][j] = self._matrix[i][j] + other._matrix[i][j]
        logger.info(f'СЛОЖЕНИЕ: {self._matrix} + {other._matrix} = {new_mtrx}')
        return Matrix(new_mtrx)

    def __mul__(self, other):
        new_mtrx = [[0 for j in range(other._clmns)] for i in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._clmns):
                for k in range(self._clmns):
                    new_mtrx[i][j] += self._matrix[i][k] * other._matrix[k][j]
        logger.info(f'УМНОЖЕНИЕ: {self._matrix} * {other._matrix} = {new_mtrx}')
        return Matrix(new_mtrx)

    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description='Матрицы')
        parser.add_argument('-m_1', type=list[list], default=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        parser.add_argument('-m_2', type=list[list], default=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        parser.add_argument('-action', type=str, default='=')

        args = parser.parse_args()

        return Matrix(args.m_1), Matrix(args.m_2), args.action


class TwoWayEqualSizeException(Exception):
    def __init__(self, first: Matrix, second: Matrix):
        self.first = first
        self.second = second

    def __str__(self):
        logger.error(f'Размерности матриц [{self.first.rows} X {self.second.rows}] и '
                     f'[{self.first.clmns} X {self.second.clmns}] не совпадают!')
        return f'Размерности матриц [{self.first.rows} X {self.second.rows}] и ' \
               f'[{self.first.clmns} X {self.second.clmns}] не совпадают!'


class OneWayEqualSizeException(Exception):
    def __init__(self, first: Matrix, second: Matrix):
        self.first = first
        self.second = second

    def __str__(self):
        logger.error(f'{self.first.clmns} != {self.second.rows} - количество столбцов одной матрицы и '
                     f'количество строк другой не равны. Операция умножения невозможна!')
        return f'{self.first.clmns} != {self.second.rows} - количество столбцов одной матрицы и ' \
               f'количество строк другой не равны. Операция умножения невозможна!'


mtrx_1 = Matrix([[2, 1], [-3, 0], [4, -1]])
mtrx_2 = Matrix([[5, -1, 6], [-3, 0, 7]])
mtrx_3 = Matrix([[2, 1], [-3, 0], [4, -1]])
mtrxs = (mtrx_1, mtrx_2, mtrx_3)
for elem in mtrxs:
    print(repr(elem))
print('---')


def main(first: Matrix, second: Matrix):
    if not Matrix._eq_len(first, second):
        raise TwoWayEqualSizeException(first, second)
    else:
        print(first == second)
        print(first + second)

    if first.clmns != second.rows:
        raise OneWayEqualSizeException(first, second)
    else:
        print(first * second)


import argparse
import logging

logging.basicConfig(filename='ex_01.log', filemode='w', encoding='utf-8',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    main(mtrx_1, mtrx_3)
    main(mtrx_1, mtrx_2)
