import numpy as np
import scipy.stats as stats

dist1a = stats.poisson.rvs(loc=18, mu=35, size=150)
dist1b = stats.poisson.rvs(loc=18, mu=25, size=100)
dist1 = np.concatenate((dist1a, dist1b))

dist2a = stats.poisson.rvs(loc=18, mu=32, size=150)
dist2b = stats.poisson.rvs(loc=18, mu=28, size=100)
dist2 = np.concatenate((dist2a, dist2b))

statistic, pvalue = stats.ttest_ind(a=dist1, b=dist2, equal_var=False)

print("Resultado do Teste t de Student:")
print(f"Estatística t: {statistic:.4f}")
print(f"Valor p (p-value): {pvalue:.4e}")
