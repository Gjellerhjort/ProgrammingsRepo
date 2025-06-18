from ..operations import arithmetic, linear_algebra

class Matrix:
    def __init__(self, data):
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length.")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])


    def shape(self):
        return (self.rows, self.cols)

    def __getitem__(self, key):
        if isinstance(key, tuple):
            i, j = key
            return self.data[i][j]
        return self.data[key]
    
    def __len__(self):
        return self.rows

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            i, j = key
            self.data[i][j] = value
        else:
            self.data[key] = value

    def __str__(self):
        return '\n'.join(['[' + ' '.join(map(str, row)) + ']' for row in self.data])
    
    def __add__(self, other):
        return arithmetic.add(self, other)
    
    def __sub__(self, other):
        return arithmetic.sub(self, other)
    
    def __mul__(self, other):
        return arithmetic.mul(self, other)
    
    def __matmul__(self, other):
        return linear_algebra.matmul(self, other)

    def dot(self, other: 'Matrix'):
        return linear_algebra.dot(self, other)
    
    def determinant(self):
        return linear_algebra.determinant(self)