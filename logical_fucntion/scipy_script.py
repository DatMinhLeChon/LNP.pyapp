# Scipy numerical library
from scipy.optimize import linprog

# Logical procesing here ...
class Model:
    def __init__(self, method_name, lhs_ineq , rhs_ineq, bnd):   
        self.obj = []
        self.lhs_ineq = lhs_ineq
        self.rhs_ineq = rhs_ineq
        self.method = method_name
        self.bnd = bnd
        
    def linearProgramming(self):
        return linprog(c= self.obj, A_ub = self.lhs_ineq, b_ub = self.rhs_ineq,\
            A_eq=self.lhs_eq, b_eq = self.rhs_eq, bounds = self.bnd,\
            method=self.method)
    
    def visualize(self):
        opt = self.linearProgramming()
    
# python3 logical_fucntion\linalg_numpy.py