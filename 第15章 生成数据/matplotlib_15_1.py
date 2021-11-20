import matplotlib.pyplot as plt

intput_values = list(range(1, 5000))
squares = [x**3 for x in intput_values]

plt.plot(intput_values, squares, linewidth = 5)
plt.title("Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("三次方", fontsize = 14)

plt.tick_params(axis='both', labelsize=14)
plt.show()
