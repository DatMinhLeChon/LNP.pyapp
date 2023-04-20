# Scipy numerical library
from scipy.optimize import linprog

""" scipy linear"""
class ModelLinear:
    def __init__(self, method_name, lhs_ineq , rhs_ineq, lhs_eq, rhs_eq, bnd):   
        self.obj = []
        # Bat đang thuc
        self.lhs_ineq = lhs_ineq
        self.rhs_ineq = rhs_ineq
        # Dang thuc
        self.lhs_eq = lhs_eq
        self.rhs_eq = rhs_eq
        self.method = method_name
        self.bnd = bnd
        
    def linearProgramming(self):
        
        return linprog(\
            c= self.obj,\
            A_ub = self.lhs_ineq,\
            b_ub = self.rhs_ineq,\
            A_eq=self.lhs_eq,\
            b_eq = self.rhs_eq,\
            bounds = self.bnd,\
            method=self.method\
            )
    
    def visualize(self):
        opt = self.linearProgramming()
        return opt.fun()
        
        
# python3 logical_fucntion\linalg_numpy.py