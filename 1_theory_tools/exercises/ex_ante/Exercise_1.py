# import packages used
import numpy as np

def solve_backwards(beta,W,T):
    
    # 2. Initialize
    Vstar_bi = np.nan+np.zeros([W+1,T])
    Cstar_bi = np.nan + np.zeros([W+1,T])
    Cstar_bi[:,T-1] = np.arange(W+1) 
    Vstar_bi[:,T-1] = np.sqrt(Cstar_bi[:,T-1])
    
    # 3. solve
    # Loop over periods
    for t in reversed(range(T-1)):  #from period T-2, until period 0, backwards  
        
        #loop over states
        for w in range(W+1):
            c = np.arange(w+1)
            
            w_next=w-c
            
            V_next=Vstar_bi[w_next,T-1]

            V_guess = np.sqrt(c)+beta*V_next #(w+1) vector of possible values next period
            Vstar_bi[w,t] = np.amax(V_guess) #Find the maximum value
            Cstar_bi[w,t] = np.argmax(V_guess) #Find the corresponding consumption (in this case equal to the index of the maximum value)

    return Cstar_bi, Vstar_bi

def simulate(Cstar,T,W):
    C_backwards = np.empty(T)
    W_now = W
    for t in range(T):
        W_now = int(W_now)   # change the type to integreger 0,1,2,3 and so on
        C_backwards[t]=Cstar[W_now,t]
        #update w
        W_next=W_now-C_backwards[t]
        W_now=W_next
        
    return C_backwards