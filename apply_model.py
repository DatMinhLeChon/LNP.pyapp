import public_var 
from model.scipy_script import ModelLinear

def applyModelLNP():
    model_lnp = ModelLinear(\
        public_var.public_obj,\
        public_var.public_lhs_ineq,\
        public_var.public_rhs_ineq,\
        public_var.public_lhs_eq,\
        public_var.public_rhs_eq,\
    )
    return model_lnp.visualize()