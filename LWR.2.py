import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def lowess_smoothing(x, y, frac=0.45):
    n = len(x)
    r = int(np.ceil(frac * n))
    yest = np.zeros(n)

    for i in range(n):
        left = max(0, i - r // 2)
        right = min(n, i + r // 2)
        x_subset = x[left:right]
        y_subset = y[left:right]
        
        # Calculate weights based on distances
        distances = np.abs(x_subset - x[i])
        weights = np.exp(-distances / (distances.max() * frac))
        
        # Fit a weighted linear regression model
        model = LinearRegression()
        model.fit(x_subset[:, np.newaxis], y_subset, sample_weight=weights)
        yest[i] = model.predict([[x[i]]])[0]  

    return yest

n = 100
x = np.linspace(0, 2 * np.pi, n)
y = np.sin(x) + 0.3 * np.random.randn(n)
yest = lowess_smoothing(x, y, frac=0.5)

plt.plot(x, y, 'r.', label='Original data')
plt.plot(x, yest, 'b-', label='LOWESS fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Locally Weighted Regression')
plt.legend()
plt.show()


