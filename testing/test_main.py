import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_variables_exist(self):
        self.assertTrue( "average" in globals(), "there is no variable called average in your code" )
        self.assertTrue( "error" in globals(), "there is no variable called error in your code" )
        
    def test_average_correct(self) :
        myblocks, myaverage = 10*[0], 0
        for i in range(10) :
            myblocks[i] = sum( eng[i*100:(i+1)*100] ) / 100 
            myaverage = myaverage + myblocks[i] 
  
        myaverage = myaverage / 10
        self.assertTrue( np.abs( myaverage - average )< 1e-7, "The final value that you have obtained for the average energy is incorrect" )
        
    def test_error_correct(self) :
        myblocks, myaverage, mysq = 10*[0], 0, 0
        for i in range(10) :
            myblocks[i] = sum( eng[i*100:(i+1)*100] ) / 100 
            myaverage = myaverage + myblocks[i] 
            mysq = mysq + myblocks[i]*myblocks[i]
  
        mysq, myaverage = mysq / 10, myaverage / 10
        myvar = ( 10 / 9 )*( mysq - myaverage*myaverage )
        myerr = np.sqrt( myvar / 10 )
        self.assertTrue( np.abs( myerr - error ) < 1e-7, "the final value you have obtained for the error is incorrect" )
