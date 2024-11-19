import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def model(x):
    return 1 / (1 + np.exp(-x))

size = 1000

x = np.random.normal(size=size)
y = (x > 0).astype(float)

x = x[:, np.newaxis]

logreg = linear_model.LogisticRegression(C=1e5, solver='lbfgs')

logreg.fit(x, y)

x_test = np.linspace(-4, 4, 400)[:, np.newaxis] 

y_pred = model(x_test * logreg.coef_ + logreg.intercept_).ravel()

plt.scatter(x, y, color='black', label='Dado original')
plt.plot(x_test, y_pred, color='red', label='Dado ajustado')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Regressão logística')
plt.show()
