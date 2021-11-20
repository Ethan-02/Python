import matplotlib.pyplot as plt

from random_walk import RandomWalk

#一直循环运行直到你不想运行他
while True:
    #创建实例，并绘制所有点
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # 设置分辨率和窗口大小
    plt.figure(dpi=128, figsize=(10, 6))
    
    #进行散点图绘制并设置颜色映射
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=1)
    #下面的代码为作业15-3分子运动内容，修改注释即可
    #plt.plot(rw.x_values, rw.y_values, linewidth=1, )
    
    #起点与终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=75)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=75)
        
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    #启动查看器
    plt.show()
    
    #判断是否继续
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
