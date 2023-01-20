import numpy as np

dim = int(input('Enter the dimensions of the matrices: '))

def matrix(number):
  matrix = []
  for a in range(number):
    row = []
    for b in range(number):
      x = int(input('Enter a number: '))
      row.append(x)
    matrix.append(row)

  matrix = np.array(matrix)
  print(f'{matrix} \t is the desired matrix')
  return matrix

def results(a,b):
  # Matrix addition
  print(f'Addition of two matrices is:\n ',a+b)

  # Matrix dot product
  print('Multiplication of two matrices is:\n ',np.dot(a,b))

results(matrix(dim),matrix(dim))