#integers Are of Arbitrary Precision

a = 10**10
print(a)

#Floating- point Precision

a = 0.1 + 0.2
print(a)

#complex numbers

a = 3 + 4j
print(a.real)
print(a.imag)

#built- in Functions for Numerical Operations

print(abs(-5))
print(round(3.14159, 2))
print(pow(2, 3))

import seaborn as sns
import matplotlib.pyplot as plt

data = [7, 15, 13, 18, 19, 10, 9, 11, 30]
sns.boxplot(data=data)

plt.title('Distribution and Outliers in Data (Box Plot)')
plt.show()

pip install seaborn


