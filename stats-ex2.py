import numpy as np
import matplotlib.pyplot as plt


mu = 0.5  
sigma = 0.1  
sample_size = 1000 
n_bins = 20 

normal_dist = np.random.normal(mu, sigma, sample_size)

count, bins, ignored = plt.hist(normal_dist, n_bins, density=True, color='red', label='Histograma')

bin_centers = 0.5 * (bins[1:] + bins[:-1])
gaussiana = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-(bin_centers - mu) ** 2 / (2 * sigma ** 2))

plt.plot(bin_centers, gaussiana, linewidth=2, color='blue', label='Curva Gaussiana')

plt.xlabel('Valores')
plt.ylabel('Densidade')
plt.title('Distribuição Normal')
plt.legend()
plt.grid(alpha=0.3)

plt.show()