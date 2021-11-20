#生成显示1~5000的整数的立方的图表
import matplotlib.pyplot as plt

intput_values = list(range(1, 5000))#创建1~5000的数字列表
cube = [x**3 for x in intput_values]#根据intput_values列表生成三次方列表

plt.title("Cube Numbers", fontsize = 24)#图表的标题
plt.xlabel("Value", fontsize = 14)#横坐标名称
plt.ylabel("Cube of Value", fontsize = 14)#纵坐标名称
plt.tick_params(axis='both', labelsize=14)#设置刻度标记的字号
plt.plot(intput_values, cube, linewidth = 5)#绘图

plt.show()#打开matplotlib查看器
