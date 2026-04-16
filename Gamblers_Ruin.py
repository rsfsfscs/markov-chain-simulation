import random
import numpy as np

#N=6    #total capital
#K=4     #player A starting capital
#p=2/5   #probability of player A win a game

#probability player A win by theory:
def probability_theory(K,N,p):
    q=1-p
    w=q/p
    PK=(1-w**K)/(1-w**N)
    return PK

#simulation of overall win or lose by conditions:
def probability_simulation(K,N,p):
    while True:
        if random.random() < p:         #next state is K+1 by probability p
            K+=1
        else:                           #next state is K-1 by probability q
            K-=1
        if K==N:                        #if K=N, player A win in this simulation 
            return 1                    
        elif K==0:                      #if K=0, player A lose in this simulation 
            return 0

#probability of win by simulate 10000 times
def estimate_win_probability(K,N,p,trials=10000):
    results = []
    for _ in range(trials):
        results.append(probability_simulation(K, N, p))
    return sum(results) / len(results)


#expected duration of the game by theory
def duration_theory(K,N,p):
    q=1-p
    w=q/p
    DK=(1/(p-q))*(N*(1-w**K)/(1-w**N)-K)  
    return DK

#simulation of the expected duration
def duration_simulate(K,N,p):
    duration_count=0
    history=[K]
    for i in range(100):
        if random.random() < p:
            K=K+1
        else:
            K=K-1
        history.append(K)
        duration_count+=1
        if K>=N or K<=0:
            break
    return duration_count

#average expected duration by repeating 10000 times
def expected_duration(K,N,p,trials=10000):
    duration=[]
    for _ in range(trials):
        duration.append(duration_simulate(K,N,p))
    return sum(duration)/len(duration)