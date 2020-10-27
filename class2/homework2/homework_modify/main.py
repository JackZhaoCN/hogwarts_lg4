import random

from class2.homework2.homework_modify.TongLao import TongLao
from class2.homework2.homework_modify.XuZhu import XuZhu

if __name__ == "__main__":
    npc1 = XuZhu(1000, 50)
    npc2 = TongLao(1000, 80)

    npc1.read()
    people = random.choice(["WYZ", "李秋水", "丁春秋"])
    print(f"TongLao遇到了{people}")
    npc2.see_people(people)
    if people == "丁春秋":
        print("开始战斗")
        ding_hp=random.randint(200, 500)
        ding_power=random.randint(20, 600)
        npc2.fight_zms(ding_hp, ding_power)
