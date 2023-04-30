"""glocal variable project-level"""

public_number_const = None
public_number_val = None

objective_type = None # 1 is maximize, 0 minimize
public_obj = None

# inequal
public_lhs_ineq = None
public_rhs_ineq = None

#equal
public_lhs_eq = None
public_rhs_eq = None

public_method = ''

values = {"Maximize" : 1, "Minimize" : 0}

# Frame 
root_main = None # global variable Frame
root_temp = None # global variable Frame 

# signal loop use to check dataset frame running
signal_loop = 1

result_lnp = None