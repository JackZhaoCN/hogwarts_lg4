'''
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''


def fight_one_round(my_hp, my_power, enemy_hp, enemy_power):
    my_new_hp = my_hp - enemy_power
    enemy_new_hp = enemy_hp - my_power
    if my_new_hp > 0 and enemy_new_hp > 0:
        if my_new_hp == enemy_new_hp:
            return 0
        elif my_new_hp > enemy_new_hp:
            return 1
        else:
            return 2
    else:
        return 0



class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self, name):
        if name == "WYZ":
            print("师弟！！！！")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")

    def fight_zms(self, enemy_hp, enemy_power):
        self.hp *= 0.5
        self.power *= 10
        print(f"我的武力增加到{self.power}, 血量减低到{self.hp}")
        result = fight_one_round(self.hp, self.power, enemy_hp, enemy_power)
        if result == 0:
            print("The fight ended in a draw! ")
        elif result == 1:
            print("TongLao win! ")
        elif result == 2:
            print("TongLao was killed by enemy! ")
