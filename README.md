# Markov Chain Simulation

A Python project for simulating and analysing discrete-time Markov chains.  
This repository combines theoretical results with Monte Carlo simulation to study transition probabilities, convergence behaviour, and applications such as Gambler’s Ruin.

---

## Overview

This project implements:

- Exact computation of n-step transition probabilities using matrix powers
- Simulation of Markov chains using random sampling
- Monte Carlo estimation of transition probabilities
- Comparison between theoretical and simulated results
- Exploration of convergence to a stationary distribution

---

## Mathematical Background

Let \( P \) be a transition probability matrix (TPM).

### n-step Transition Probabilities

The probability of moving from state \( i \) to state \( j \) in \( n \) steps is:

$$
P^n_{ij}
$$

This is computed using matrix powers:
```python
np.linalg.matrix_power(P, n)
```

### Initial Distribution

If the initial state follows a distribution p, then the distribution after n steps is:

$$
pP^n
$$

This represents the probability distribution over all states at time n.

### Simulation Interpretation
We simulate a Markov chain by:
- Choosing an initial state
- Sampling transitions using the TPM
- Repeating for n steps
- Estimating probabilities via repeated trials

---
## Features
### Theoretical Computation
```python
Pnij(TPM, n, i, j)
```
To computes the exact value of $P^n_{K,i}$
```python
pPnij(p, TPM, n)
```
To computes $p^n_i=(pP^n)_i$​

### Simulation
```python
Pnij_simulation(TPM,n,i,j,trials=10000)
```
Estimates $P^n_{K,i}$ using Monte Carlo methods
```python
pPnij_simulation(p,TPM,n,trials=10000)
```
Estimates probabilities when the initial state is random

### Efficient Sampling
The project uses cumulative transition probabilities and np.searchsorted to identify the random sampling.

---
## Experiments
### Theory vs Simulation

We compare theoretical results with Monte Carlo estimates.

#### Relative Error

$$
\text{Error} = \frac{| \hat{P} - P |}{|P|}
$$

#### Distribution Comparison

We compare the full distribution:

$$
pP^n \quad \text{vs} \quad \hat{pP^n}
$$

#### Example Result

```python
Pnij= 0.27777777777777773
Pnij_simulation= 0.2819
relative_error= 0.0148400000000001
pPnij= [0.33888889 0.23888889 0.42222222]
pPnij_simulation= [0.3394 0.2408 0.4198]
distribution_comparison= 0.0031274175833650155
```

The simulation closely matches the theoretical distribution:

- Small relative error

### Convergence of Markov Chains
A key property of Markov chains is convergence to a stationary distribution.

This occurs when the chain is:

- Irreducible (all states communicate)
- Aperiodic (no fixed cycles)

We test with matrix:

$$
P =
\begin{pmatrix}
0.9 & 0.1 \\
0.5 & 0.5
\end{pmatrix}
$$

![Convergent](images/convergent.png)

Non-Convergent Example

$$
P =
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
$$

![Non-convergent](images/non-convergent.png)

### Application: Gambler’s Ruin
This project also explores the Gambler’s Ruin problem, an example of an absorbing Markov chain.

- States represent the gambler’s capital
- Boundary states are absorbing (ruin or success)
- The model can be used to study:
  - Probability of ruin
  - Expected duration until absorption

This demonstrates how Markov chains apply to real-world stochastic processes

In general a Gampler's Ruin problem can be present by a TPM as follow:

$$
P =
\begin{pmatrix}
1 & 0 & 0 & 0 & ... & 0 \\
q & 0 & p & 0 & ... & 0 \\
0 & q & 0 & p & ... & 0 \\
...&...&...&...&...&... \\
0 & ... & 0 & q & 0 & p \\
0 & 0 & 0 & 0 & ... & 1 
\end{pmatrix}
$$

where p is the probability of winning the round and q is lose the round which is 1-p

By theory the probability of winning the whole game ( other player out of capital) can be find by

$$ P_k=\frac{1-(\frac{q}p)^K}{1-(\frac{q}p)^N}
$$

Therefore if we simlate using P enough times, we should get a result close to the theory

We test it with total capital N = 5, initial state 2 and probability of winning the round p = 2/3

by taking 20 step for TPM method, we get result below which are very close

```python
By TPM theory = 0.7997594170721426
simulate by TPM = 0.8002
By theory = 0.7741935483870966
simulate = 0.7797
```
