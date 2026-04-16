import numpy as np

#by theorem P^n_ij
def Pnij(TPM,n,i,j):
    Pn=np.linalg.matrix_power(TPM,n)
    return Pn[i,j]

# Use cumulative probabilities to sample next state efficiently
# This avoids manually checking each transition probability
def cumulative_TPM(TPM):
    cumulative=np.zeros(TPM.shape)
    for i in range(TPM.shape[0]):
        cumulative[i,0] = TPM[i,0]
        for j in range(1,TPM.shape[1]):
            cumulative[i,j] = cumulative[i,j-1] + TPM[i,j]
    return cumulative
#print(cumulative_TPM(TPM))

def simulate_markov(TPM,n,i):
    states = [i]
    cumulative = cumulative_TPM(TPM)
    current = i
    for _ in range(n):
        r = np.random.random()
        current = np.searchsorted(cumulative[current], r)
        states.append(current)
        
    return states

def Pnij_simulation(TPM,n,i,j,trials=10000):
    output=[]
    for _ in range(trials):
        result=simulate_markov(TPM,n,i)
        if result[n]==j:
            Pnij=1
        else:
            Pnij=0    
        output.append(Pnij)
    probability=sum(output)/len(output)
    return probability

#Until now we assume that the probability of the initial entry is K is 1 other entry 0
#Let the initial entry K is define by a vector p which is row stochastic probability
#What If I randomly start according to p, where do I end up after n steps?

#by theorem p^n_i=(pP^n)_i, for p the initail probability vector
def pPnij(p,TPM,n):
    pPn=p@np.linalg.matrix_power(TPM,n)
    return pPn

def pPnij_simulation(p,TPM,n,trials=10000):
    counts = np.zeros(len(p))
    cumulative = cumulative_TPM(TPM)
    for _ in range(trials):
        # sample initial state
        current = np.searchsorted(np.cumsum(p), np.random.random())
        
        # simulate n steps
        for _ in range(n):
            r = np.random.random()
            current = np.searchsorted(cumulative[current], r)
        #count the end state
        counts[current] += 1
    
    return counts / trials
