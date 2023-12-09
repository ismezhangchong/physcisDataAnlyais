import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

xi = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
yi = [0.5915, 0.5695, 0.557, 0.547, 0.538, 0.5265, 0.516, 0.505, 0.4945, 0.483, 0.472]
Xi = np.array(xi)
Yi = np.array(yi)


# 定义你想要拟合的函数形式，这里是反比例函数
def func(x, a, b):
    return a * x + b


# 使用curve_fit函数进行拟合，popt为拟合参数
popt, pcov = curve_fit(func, Xi, Yi)

# 创建一个用于绘图的x值数组
x_plot = np.linspace(min(Xi), max(Xi), 1000)

# 使用拟合参数计算y值
y_plot = func(x_plot, *popt)

# 绘制原始数据
plt.scatter(Xi, Yi, label='Data')

for i in range(len(Xi)):
    plt.annotate(f'({Xi[i]}, {Yi[i]})', (Xi[i], Yi[i]))

# 绘制拟合曲线
plt.plot(x_plot, y_plot, 'r', label='Fit: a=%5.3f, b=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
