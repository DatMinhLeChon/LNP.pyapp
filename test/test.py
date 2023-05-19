#function test - testcase
import random 
import logging
from model.scipy_script import ModelLinear
# create logger with 'spam_application'
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
# create file handler which logs even debug messages
file_handler = logging.FileHandler('test/test.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class Test:
    def __init__(self, obj, lhs_eq, rhs_eq, lhs_ineq, rhs_ineq  ):
        self.obj = obj
        self.lhs_eq = lhs_eq
        self.rhs_eq = rhs_eq
        self.lhs_ineq = lhs_ineq
        self.rhs_ineq = rhs_ineq

class TestCase:
    
    def __init__(self, number_test):
        self.number_test = number_test
        self.test_list = []
        
    def randomTestList(self):
        for index in range(self.number_test):
            obj, lhs_eq, rhs_eq, lhs_ineq, rhs_ineq= [], [], [], [], []
            number_constrain, number_variable = random.randrange(2,10), random.randrange(2,10)
            number_eq= random.randrange(0, number_constrain)
            for index in range(number_variable):
                obj.append(random.randrange(-10, 10))
            for index in range(number_eq):
                temp = []
                for index_val in range( number_variable): temp.append(random.randrange(-10,10))
                lhs_eq.append(temp)
                rhs_eq.append(random.randrange(-10,10))
            for index in range(number_constrain - number_eq):
                temp = []
                for index_val in range(number_variable): temp.append(random.randrange(-10,10))
                lhs_ineq.append(temp)
                rhs_ineq.append(random.randrange(-10,10))
            self.test_list.append(Test(obj, lhs_eq, rhs_eq, lhs_ineq, rhs_ineq))
    
    def getTestData(self):
        return [self.obj, \
                self.lhs_eq,\
                self.rhs_eq,\
                self.lhs_ineq,\
                self.rhs_ineq]
    
    def applyTestCMD(self):
        for (item, index) in zip(self.test_list, range(len(self.test_list))):
            try:
                
                test_apply = (item.obj, item.lhs_ineq , item.rhs_ineq, item.lhs_eq, item.rhs_eq)
                if test_apply:
                    logger.info("Test "+ str(index) + " pass")
                else: logger.info("Test "+ str(index) + " fail")
            except:
                logger.info("Test "+ str(index) + " fail")
    
    def applyTestResultFrame(self):
        return 

if __name__ == "__main__":
    test = TestCase(100)
    test.randomTestList()
    test.applyTestCMD()






