from unittest import TestCase
from robot_paths import *


class Test(TestCase):
	def test_robotPaths3x4(self):
		matrix = [[0] * 4] * 3
		result = robotPaths(matrix)
		self.assertEqual(result, 38)
	
	def test_robotPaths2x3(self):
		matrix = [[0] * 3] * 2
		result = robotPaths(matrix)
		self.assertEqual(result, 4)
	
	def test_robotPaths5x8(self):
		matrix = [[0] * 8] * 5
		result = robotPaths(matrix)
		self.assertEqual(result, 7110272)
	
	def test_robotPaths5x1(self):
		matrix = [[0] * 1] * 5
		result = robotPaths(matrix)
		self.assertEqual(result, 1)
	
	def test_robotPaths1x6(self):
		matrix = [[0] * 6]
		result = robotPaths(matrix)
		self.assertEqual(result, 1)
	
	def test_robotPaths2x2(self):
		matrix = [[0] * 2] * 2
		result = robotPaths(matrix)
		self.assertEqual(result, 2)
