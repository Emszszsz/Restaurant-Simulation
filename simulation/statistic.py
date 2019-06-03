import numpy as np
import matplotlib.pyplot as plt
"""
numpy.random.exponential : Draw samples from an exponential distribution.
numpy.random.normal: Draw random samples from a normal (Gaussian) distribution.
"""
mean_b = 3200
std_b = 100
lambda_p = 200
mean_a = 1900
std_a = 200
lambda_n = 300
lambda_j = 1700
lambda_f = 1900
table_cashier = [int(np.random.exponential(lambda_p)) for i in range(1000)]
table_buffet = [abs(int(np.random.normal(mean_b, std_b))) for i in range(1000)]
table_appear = [abs(int(np.random.normal(mean_a, std_a))) for i in range(1000)]
table_drink_end = [int(np.random.exponential(lambda_n)) for i in range(1000)]
table_food_end = [int(np.random.exponential(lambda_j)) for i in range(1000)]
table_dinner_end = [int(np.random.exponential(lambda_f)) for i in range(1000)]
"""
plt.hist(table_dinner_end, bins=20)
plt.title("Exponential distribution histogram (dinner end time)")
plt.show()
"""
