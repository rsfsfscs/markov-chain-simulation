from Gamblers_Ruin import probability_theory,estimate_win_probability,duration_theory,expected_duration
from Markov_Chain import Pnij,Pnij_simulation,pPnij,pPnij_simulation
import numpy as np
import matplotlib.pyplot as plt

TPM1=np.array([[0,1/2,1/2],[1/2,0,1/2],[1/3,1/3,1/3]])
p1=[3/5,1/5,1/5]
TPM2 = np.array([[0,0.9,0,0,0,0.1],[0,0.5,0.4,0,0,0.1],[0,0,0.6,0.2,0.1,0.1],[0,0,0.4,0.5,0,0.1],[0,0,0.4,0,0.5,0.1],[0,0,0,0,0,1]], dtype=float)
p2=[1/6,1/6,1/6,1/6,1/6,1/6]
# Construct transition probability matrix for Gambler's Ruin
def gamblers_ruin_TPM(N,p):
    # States 0 and N are absorbing (game ends)
    q=1-p
    TPM=np.zeros((N,N))
    TPM[0,0]=1
    TPM[N-1,N-1]=1
    for i in range(1,N-1):
        for j in range(0,N):
            if j==i-1:
                TPM[i,j]=q
            elif j==i+1:
                TPM[i,j]=p
    return TPM

def plot_state_probabilities(TPM, i, steps=10):
    for j in range(len(TPM)):
        probs=[]
        for p in range(steps):
            probs.append(Pnij_simulation(TPM,p,i,j))
        x=list(range(1,len(probs)+1))
        plt.plot(x,probs, label=f"State {j}")

    plt.legend()
    plt.xlabel("Number of steps (n)")
    plt.ylabel(f"P(X_n = i | X_0 = {i})")
    plt.title("Markov Chain State Probability Over Time")
    plt.grid()
    plt.show()


#example1
print(Pnij(TPM1,2,2,1))
print(Pnij_simulation(TPM1,2,2,1))
print(pPnij(p1,TPM1,2))
print(pPnij_simulation(p1,TPM1,2))
print(plot_state_probabilities(TPM1,2))
#example2
print(Pnij(TPM2,2,2,5))
print(Pnij_simulation(TPM2,2,2,5))
print(plot_state_probabilities(TPM2,2))
#example3 Gamblers Ruin
print(Pnij(gamblers_ruin_TPM(5,2/3),10,2,4))
print(Pnij_simulation(gamblers_ruin_TPM(5,2/3),10,2,4))
print(probability_theory(2,5,2/3))
print(estimate_win_probability(2,5,2/3))
