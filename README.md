# Monte Carlo Option Pricer

A Python project built while learning about options pricing and Monte Carlo 
simulation. Implements GBM-based price path simulation to price European 
put and call options.

Built as a starting point — plan to rebuild and extend this properly after 
studying probability and stochastic processes formally.

## Features
- Simulates stock price paths using Geometric Brownian Motion
- Prices European put and call options
- Visualises simulated price paths

## Example output

- S0: 100 | K: 105 | T: 1yr | r: 0.05 | vol: 0.2 | steps: 252 | sims: 10000

<img width="1599" height="824" alt="image" src="https://github.com/user-attachments/assets/e3b7d0de-1a0f-418d-bc62-1d91b290ae57" />

## Requirements

numpy, matplotlib

## What I want to add next

- Black-Scholes analytical price as benchmark for MC convergence
- Confidence intervals on the MC estimate
- Variance reduction via antithetic variates
- Greeks computation via finite difference

