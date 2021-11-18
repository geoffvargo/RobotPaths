import math
import os
import random
import re
import sys

from termcolor import colored


#
# Complete the 'robotPaths' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def robotPaths(matrix):
	print(matrix)


if __name__ == '__main__':
	# fptr = open(os.environ['OUTPUT_PATH'], 'w')
	
	i_1 = input()
	print(colored(i_1, color='green'))
	matrix_rows = int(i_1.strip())
	i_2 = input()
	print(colored(i_2, color='green'))
	matrix_columns = int(i_2.strip())
	
	matrix = []
	
	for _ in range(matrix_rows):
		i_3 = input()
		print(colored(i_3, color='green'))
		matrix.append(list(map(int, i_3.rstrip().split())))
	
	result = robotPaths(matrix)
	
	print(result)
