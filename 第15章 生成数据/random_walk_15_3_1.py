from random import choice

class RandomWalk():
    """一个创建随机漫步的类"""
    
    def __init__(self, num_points=5000):
        """基础属性"""
        self.num_points = num_points
        
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):#此处完成了作业15.3重构的内容
        """随机方向和距离"""#更改下面两行代码可以完成作业15.2改进随机漫步的内容
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """随机漫步所有点"""
        
        # 一直漫步直到列表达到指定大小
        while len(self.x_values) < self.num_points:
            
            #获得本次随机坐标
            x_step = self.get_step()
            y_step = self.get_step()
            
            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            
            #在列表中加入本次随机的点
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
