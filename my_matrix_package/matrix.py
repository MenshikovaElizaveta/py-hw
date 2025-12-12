class Matrix:
    def __init__(self, rows, cols, data = None):
        self.rows = rows
        self.cols = cols
        
        if data:
            self.data = data
        else:
            self.data = []
            for i in range(rows):
                row = [0] * cols  # строка из нулей
                self.data.append(row)


    def __matmult__(self, other):

        if (self.cols != other.rows):
            raise ValueError("Число столбцов первой матрицы должно равняться числу строк второй матрицы")
   
        result = Matrix(self.rows, other.cols)

        for i in range(self.rows):
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.data[i][k] * other.data[k][j]
                result.data[i][j] = total


        return result



    def __nummult__(self, num):
        result = Matrix(self.rows, self.cols)

        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] * num

        return result     
    

    def __add__(self, other):
        result = Matrix(self.rows, self.cols)
        
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        
        return result
    