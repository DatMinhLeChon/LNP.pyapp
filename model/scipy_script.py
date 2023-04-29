# Scipy numerical library
from scipy.optimize import linprog

""" scipy linear"""
class ModelLinear:
    def __init__(self, obj, lhs_ineq , rhs_ineq, lhs_eq, rhs_eq):   
        self.obj = obj
        # Bat đang thuc
        self.lhs_ineq = lhs_ineq
        self.rhs_ineq = rhs_ineq
        # Dang thuc
        self.lhs_eq = lhs_eq
        self.rhs_eq = rhs_eq
        self.method = "highs-ds"
        
        
    def linearProgramming(self):
        if self.lhs_eq == []:
            return linprog(\
                c= self.obj,\
                A_ub = self.lhs_ineq,\
                b_ub = self.rhs_ineq,\
                method=self.method\
                )
        elif self.lhs_ineq ==[]:
            return linprog(\
                c= self.obj,\
                A_eq=self.lhs_eq,\
                b_eq = self.rhs_eq,\
                method=self.method\
                )
        else:
            return linprog(\
                c= self.obj,\
                A_ub = self.lhs_ineq,\
                b_ub = self.rhs_ineq,\
                A_eq=self.lhs_eq,\
                b_eq = self.rhs_eq,\
                method=self.method\
                )
    
    def visualize(self):
        opt = self.linearProgramming()
        return opt
        
        
# python3 logical_fucntion\linalg_numpy.py