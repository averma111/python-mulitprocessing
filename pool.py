from multiprocessing import Pool
import math
import time

N = 5000000

def cube(x):
    return math.sqrt(x)

if __name__ == "__main__":
    with Pool() as pool:
      result = pool.map(cube, range(10,N))
    print("Program finished!")