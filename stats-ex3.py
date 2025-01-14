from scipy.stats import binom, gaussian_kde
import matplotlib.pyplot as plt
import numpy as np

binomial_dist = binom.rvs(n=20,p=0.8,loc=0,size=1000)

n_bins = 20
count, bins, ignored = plt.hist(binomial_dist, n_bins, density=True, color='red')


densidade = gaussian_kde(binomial_dist)
xs = np.linspace(0,n_bins,200)
densidade._compute_covariance()

plt.plot(xs,densidade(xs))
plt.xlabel('Binomial')
plt.ylabel('Frequencia')
plt.title('Distribuição binomial')
plt.show()