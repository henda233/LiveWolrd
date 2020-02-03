import random

class Player:
    def __init__(self,name,areas):
        self.name=name
        self.body=10
        self.buff=["None"]
        self.money=random.randint(0,10000)
        self.hunger=40
        self.nutrition=40
        self.sleep=48
        self.power=random.randint(1,10)
        self.speed=random.randint(1,10)
        self.army=["head","body","foot"]
        self.protect_army = [0,0,0]
        self.protect_infection=0
        self.skill=[0,0,0,0,0]#shot,drive,making,building,fight
        self.move_point=10
        self.misson="None"

        self.manc() #选择角色

        self.data_areas=areas

        self.areac()
        print("角色创建完毕。")
    def manc(self):
        a=random.randint(1,3)
        if a==1:
            self.man="百姓"
        elif a==2:
            self.man="警察"
        else:
            self.man="军人"

    def areac(self):
        a=random.randint(0,5)
        self.area=self.data_areas[a]