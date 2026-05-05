import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom


n = 20        
p = 0.5       
trials = 1000 


data = np.random.binomial(n, p, trials)


x = np.arange(0, n + 1)
pmf = binom.pmf(x, n, p)


plt.figure(figsize=(10, 6))
plt.hist(data, bins=np.arange(-0.5, n + 1.5, 1), density=True, alpha=0.6, 
         color='skyblue', edgecolor='black', label='Empiryczne (Symulacja)')
plt.stem(x, pmf, linefmt='r-', markerfmt='ro', basefmt=" ", label='Teoretyczne B(20, 0.5)')

plt.title(f'Porównanie symulacji ({trials} prób) z rozkładem dwumianowym')
plt.xlabel('Liczba sukcesów (orłów)')
plt.ylabel('Prawdopodobieństwo')
plt.legend()
plt.show()