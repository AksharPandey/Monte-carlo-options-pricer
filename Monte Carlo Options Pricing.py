import numpy as np
import matplotlib.pyplot as plt


S0 = float(input("Enter Current Stock Price: "))  # Starting Stock Price
K = float(input("Enter end price: "))  # Strike Price - Allowed to buy at this price
T = float(input("Enter time to expiration (Years): "))  # Time to expiration
r = float(input("Enter risk free rate: "))  # Risk-free rate
vol = float(input("Enter stock volatility: "))  # Stock volatility
steps = int(input("Enter number of increments: "))  # Steps
sims = int(input("Enter amount of simulations: "))  # Number of simulations
pc = input("Enter Put/Call Option: ")


dt = T/steps  # Time Per Step
drift = (r-(vol**2)/2)*dt  # Predictable Change


Sims = np.random.normal(0, 1, (sims,  steps)) * vol * np.sqrt(dt) + drift
# 2D list containing multiple simulations of price change

CumSum = np.exp(np.cumsum(Sims, axis=1)) * S0
#Cumulative Sum across time axis scaled across Current Stock Price

prices = CumSum[:, -1]
# Get an array of final price of all days

if pc.upper() == 'PUT':
    payoff = np.maximum(K - prices, 0)
elif pc.upper() == 'CALL':
    payoff = np.maximum(prices - K, 0)
else:
    print("Invalid Option provided, going with 'PUT'")
    payoff = np.maximum(K - prices, 0)

# Remove all non-negative values to 0, changes based on users input of Put or Call

print("The Option price is", np.mean(payoff) * np.exp(-r*T))
# Discount factor so -r * T is amount of discounting

plt.plot(CumSum[:50, :].T)
plt.show()









