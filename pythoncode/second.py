import yaml


class Animal():
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def yell(self):
        print(f"{self.name} is yelling")

    def run(self):
        print(f"{self.name} is running")


class cat(Animal):
    def __init__(self, name, color, age, sex, hair):
        super(cat, self).__init__(name, color, age, sex)
        self.hair = hair

    def skill(self):
        print(f"{self.name} 捉到了老鼠")

    def jump(self):
        print(f"{self.name} 喵喵叫")


class dog(Animal):
    def __init__(self, name, color, age, sex, hair):
        super(dog, self).__init__(name, color, age, sex)
        self.hair = "短发"

    def home(self):
        print(f"{self.name}能看家")

    def yell(self):
        print(f"{self.name} 汪汪叫")


if __name__ == "__main__":
    with open("data.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        print(datas)
        cat11 = datas['cat1']
        dog11 = datas['dog1']
        cat1 = cat("小猫", "蓝色", 12, "男", "短发")
# 不使用yaml管理类属性的写法：cat1=cat("小猫","蓝色",12,"男","短发")
print(f"{cat11['name']}的颜色是{cat11['color']} ,年龄是{cat11['age']},性别{cat11['sex']},{cat11['hair']}")
cat1.skill()
print("---------------------------------------------------")
# 不使用yaml管理类属性的写法:dog1=dog("小狗","白色",10,"女","长发")
dog1 = dog("小狗", "白色", 10, "女", "长发")
print(f"{dog11['name']}的颜色是{dog11['color']} ,年龄是{dog11['age']},性别{dog11['sex']},{dog11['hair']}")
dog1.home()
