# 定义一个类
class people():
    alive = True

    def __init__(self,_name):
        self.name = _name


p1 = people("xioa")
p2 = people("da")
print(p1.name, p2.name, people.alive, p1.alive, p2.alive)
people.alive = "qq"
print(p1.name, p2.name, people.alive, p1.alive, p2.alive)

