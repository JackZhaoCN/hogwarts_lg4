"""
写一个Glass(玻璃杯)类,有fill(注水)方法,
调用时显示当前水量(当前水量为ml):
1. fill(ml) 表示注水
"""


# 玻璃杯类
class Glass:
    def __init__(self, color, volume, quality):
        self.color = color
        self.volume = volume
        self.quality = quality
        self.density = quality / volume

    def show_glass_type(self):
        if self.density > 4:
            print(f"This is a {self.color} high quality glass")
        else:
            print(f"Don't buy this {self.color} glass")


if __name__ == "__main__":
    test_glass = Glass(input("what's the color of this glass"), int(input("what's the volume of the glass (ml)")),
                       int(input("what's the quality of the glass (g)")))
    test_glass.show_glass_type()
