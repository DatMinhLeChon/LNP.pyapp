"""glocal variable project-level"""

public_number_const = None
public_number_val = None

objective_type = None # 1 is maximize, 0 minimize

# inequal
public_lhs_ineq = {}
public_rhs_ineq = {}

#equal
public_lhs_eq = {}
public_rhs_eq = {}

public_method = ''
public_bnd = ''
values = {"Maximize" : 1, "Minimize" : 0}

# Frame 
root_main = None # global variable Frame
root_temp = None # global variable Frame 

# signal loop use to check dataset frame running
signal_loop = 1

result_lnp = None