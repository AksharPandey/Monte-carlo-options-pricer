# Monte Carlo Option Pricer

A Python implementation of Monte Carlo simulation for pricing European put 
and call options, built after studying how stochastic price path simulation 
works conceptually.

## What it does

Prices a European option by simulating thousands of possible future stock 
price paths and averaging the discounted payoff across all of them.

The core idea: instead of solving for the option price analytically, we 
simulate the randomness of the market directly. Each path represents one 
possible future for the stock price, evolving according to Geometric 
Brownian Motion — the standard model for stock price dynamics, which 
captures both the expected drift of the stock and its random volatility.

At expiry, we calculate what the option would pay off on each path, then 
discount the average back to today using the risk-free rate. With enough 
simulations, this converges to the true option price.

## Features

- Simulates GBM price paths using numpy vectorisation
- Prices both European put and call options
- Visualises the first 50 simulated price paths
- User-defined inputs: stock price, strike, expiry, rate, volatility, 
  steps, simulations

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

