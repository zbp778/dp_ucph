# import packages used
import numpy as np
import scipy.optimize as optimize

def solve_consumption_grid_search(par):
     # initialize solution class
    class sol: pass
    sol.C = np.zeros(par.num_W)
    sol.V = np.zeros(par.num_W)
    
    # consumption grid as a share of available resources
    grid_C = np.linspace(0.0,1.0,par.num_C) 
    
    # Resource grid
    grid_W = par.grid_W

    # Init for VFI
    delta = 1000 #difference between V_next and V_now
    sol.it = 0  #iteration counter 
    
    while (par.max_iter>= sol.it and par.tol<delta):
        sol.it = sol.it+1
        V_next = sol.V.copy()
        for iw,w in enumerate(grid_W):  # enumerate automaticcaly unpack w
            grid_C_adap=grid_C*w
            util=np.sqrt(grid_C_adap)
            W_next=w-grid_C_adap
            #Next period's value
            interp=np.interp(W_next,grid_W,sol.V) # Can I actually use sol.V here or should I use V_next?
            V_guess=util+par.beta*interp
            #Update with new max
            sol.V[iw]=np.max(V_guess)
            sol.C[iw]=grid_C_adap[np.argmax(V_guess)]                            
        delta = np.amax(np.abs(sol.V - V_next))
    
    return sol