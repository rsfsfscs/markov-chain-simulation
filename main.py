from Gamblers_Ruin import probability_theory,estimate_win_probability,duration_theory,expected_duration
from Markov_Chain import Pnij,Pnij_simulation,pPnij,pPnij_simulation
import numpy as np
import matplotlib.pyplot as plt

TPM1 = np.array([[0,1/2,1/2],[1/2,0,1/2],[1/3,1/3,1/3]])
p1=[3/5,1/5,1/5]
TPM2 = np.array([[0.9,0.1],[0.5,0.5]])
TPM3 = np.array([[0,1],[1,0]])
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

def Convergence_plot(TPM,n,i,j):
    errors = []
    Ns=np.logspace(2, 5, 20, dtype=int)  # 100 → 100000
    for N in Ns:
        theory = Pnij(TPM, n, i, j)
        sim = Pnij_simulation(TPM, n, i, j, trials=N)
        errors.append(abs(sim - theory))
    plt.plot(Ns, 1/np.sqrt(Ns), linestyle='--', label='O(1/sqrt(N))')
    plt.legend()
    plt.plot(Ns,errors)
    plt.title("Error vs N")
    plt.xlabel("Simulate trials N")
    plt.ylabel("Absolute Error")
    plt.show()

def relative_error(theory,sim):
    return abs(sim - theory) / abs(theory)
def distribution_comparison(theory,sim):
    return np.linalg.norm(sim - theory)

#Part1 Theory vs Simulation
Pn=Pnij(TPM1,2,2,1)
Pn_simulation=Pnij_simulation(TPM1,2,2,1)
print('Pnij=',Pn)
print('Pnij_simulation=',Pn_simulation)
print('relative_error=',relative_error(Pn,Pn_simulation))
pPn=pPnij(p1,TPM1,2)
pPn_simulation=pPnij_simulation(p1,TPM1,2)
print('pPnij=',pPn)
print('pPnij_simulation=',pPn_simulation)
print('distribution_comparison=',distribution_comparison(pPn,pPn_simulation))
print(Convergence_plot(TPM1,2,1,1))
#Part2 convergence
print(Pnij(TPM2,2,1,1))
print(Pnij_simulation(TPM2,2,1,1))
print(plot_state_probabilities(TPM2,0,steps=15))
print(plot_state_probabilities(TPM3,0,steps=15))
#Part3 Gamblers Ruin
print('By TPM theory =',Pnij(gamblers_ruin_TPM(5,2/3),20,2,4))
print('simulate by TPM =',Pnij_simulation(gamblers_ruin_TPM(5,2/3),20,2,4))
print('By theory =',probability_theory(2,5,2/3))
print('simulate =',estimate_win_probability(2,5,2/3))
