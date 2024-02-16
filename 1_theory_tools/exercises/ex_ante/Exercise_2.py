# import packages used
import numpy as np

def solve_VFI(par):
    grid_W = np.arange(par.W+1) #Make a W+1 dimensional grid of possible cake sizes
    Cstar = np.zeros([par.W+1]) #Make a W+1 dimensional grid of optimal consumption choices
    
    # Parameters for VFI
    max_iter = par.max_iter   # maximum number of iterations
    delta = 1000 #difference between V_next and V_now
    tol = par.tol #convergence tol. level
    it = 0  #iteration counter 
    V_now = np.zeros([par.W+1]) #arbitrary starting values
    
    while (max_iter>= it and tol<delta):
        it = it+1
        V_next = V_now.copy()
        for w in range(par.W+1):
            # Fill in
            # Hint: Same idea as Exercise 1 with Backward Induction, but now without time dimension
            c = grid_W[0:w+1] # vector with 0 to w 
            w_next = w-c 

            V_guess=np.sqrt(c) + par.beta * V_next[w_next]

            V_now[w] = np.amax(V_guess) #Find the maximum value
            Cstar[w] = np.argmax(V_guess) #Find the corresponding consumption (in this case equal to the index of the maximum value)

        delta = np.amax(np.abs(V_now - V_next)) #Compute maximum difference between V_next and V_now
    
    class sol: pass
    sol.C = Cstar
    sol.V = V_now
    sol.it = it

    return sol

# define function
def simulate(Cstar,T,W):
    C_vfi = np.zeros(T)
    W_now = W
    for t in range(T):
        W_now = int(W_now)   # change the type to integreger 0,1,2,3 and so on
        C_vfi[t]=Cstar[W_now]
        W_now = W_now-C_vfi[t]
    return C_vfi
