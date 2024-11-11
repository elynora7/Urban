import requests
import numpy as np
from matplotlib import pyplot as plt

response = requests.get('https://api.github.com')

print(response.status_code)
print(response.headers)
print(response.json())

print('--------------------')

arr = np.array([8, 6, 4, 9, 1, 2, 5])
arr = np.sort(arr)
arr = arr ** 2
print(arr)
print(f'Сумма: {np.sum(arr)}')

print('--------------------')

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('График')
plt.grid(True)
plt.show()


