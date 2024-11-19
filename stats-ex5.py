from scipy.stats import bernoulli, gaussian_kde
import matplotlib.pyplot as plt
import numpy as np

bernoulli_dist = bernoulli.rvs(size=1000,p=0.6)

n_bins = 10
count, bins, ignored = plt.hist(bernoulli_dist, n_bins, density=True, color='red')


densidade = gaussian_kde(bernoulli_dist)
xs = np.linspace(0,2,200)
densidade._compute_covariance()

plt.plot(xs,densidade(xs))
plt.xlabel('Bernoulli')
plt.ylabel('Frequencia')
plt.title('Distribuição Bernoulli')
plt.show()