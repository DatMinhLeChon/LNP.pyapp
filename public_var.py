"""glocal variable project-level"""

public_number_const = None
public_number_val = None

objective_type = None # 1 is maximize, 0 minimize
public_obj = None #objective array 1D

# inequal
public_lhs_ineq = None # inequal left side array 2D
public_rhs_ineq = None # inequal right side array 1D

#equal
public_lhs_eq = None # equal left side array 2D
public_rhs_eq = None # equal right side array 1D

public_method = '' #base: "hight-ds" method

values = {"Maximize" : 1, "Minimize" : 0} # value in radiobutton, configuration frame

# Frame 
root_main = None # global variable Frame
root_temp = None # global variable Frame 

# signal loop use to check dataset frame running
signal_loop = 1 # check table create in main frame, if already init, close configuration frame 

result_lnp = None # model variable