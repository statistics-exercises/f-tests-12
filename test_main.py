import unittest
import scipy.stats
from main import *

class UnitTests(unittest.TestCase) :
    def test_gen_f_var(self) : 
        for i in range(2,5) :
            for j in range(10,15) :
                t = gen_f_variable( i, j )
                pval = scipy.stats.f.cdf( t, i-1, i*j-i )
                self.assertTrue( pval<0.99, "Your program for generating the statistic is not working correctly.  I test this code by performing a hypothesis test with a 1% significance level.  There is thus a small probability your code is correct even if this test shows up as failing." )
