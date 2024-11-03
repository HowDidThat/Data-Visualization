import unittest
import matplotlib
import csv

def solveHereTherory():
    pass
def solveHereExerciseAlone():
    pass


class test(unittest.TestCase):
    def testFunctionSolve(self):
        result = solveHereExerciseAlone()
        self.assertEqual(result,{'platform': ['PS4', 'XOne', 'PC', 'WiiU'], 'na_sales': [98.6100000000001, 81.27000000000007, 7.229999999999998, 19.36000000000001], 'eu_sales': [130.0400000000001, 46.25000000000001, 17.970000000000045, 13.149999999999995], 'jp_sales': [15.05999999999997, 0.32000000000000006, 0.0, 7.309999999999998]})

    def testTheory(self):
        result = solveHereTherory()
        self.assertEqual(result,{'year': [2014, 2015, 2016], 'critic_review': [71.0, 73.0, 73.0], 'user_review': [67.0, 68.0, 67.0]})