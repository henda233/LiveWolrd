import random,math

city_names=["石阡","上海","贵阳","北京","铜仁","六盘水"]
class City:
    def __init__(self):
        self.name=random.choice(city_names)
        self.areas = []
        for i in range(0,5):
            area_now=Area(i)
            self.areas.append(area_now)
        print("区域创建完毕，一共 6 个")
        #选择感染的地方
        a=random.randint(0,5)
        self.areas[a].zombies=1
        print("地区:"+self.areas[a].name+"  有感染体！")

    def rback(self):
        return self.areas


names = ["0", "2", "3","4","5"]

class Area:
    def __init__(self,number):
        self.number=number
        self.name=random.choice(names)
        names.remove(self.name)
        #人数
        self.breakday=1
        self.infection=random.randint(10,50)
        self.deadtion=random.randint(10,50)
        self.people=random.randint(100000,200000)
        self.infecter=0
        self.poilces=10000
        self.army=20000
        self.zombies=0
        self.dead_zombies=0
        self.dead_people=0
        self.R0=3
        self.infecter_speed=2
        self.order=100
        self.things=0 #1 1级混乱.....
        self.move=0
        self.govement_speed=random.randint(1,7)
        self.wall_build=0 #0 no 1 yes
        self.wall_strong=random.randint(10,100)
        self.work_out_step()

    def work_out_step(self):
        #概率计算
        self.dead_people_out=math.ceil(self.dead_people/self.people)
        self.infecter_out=math.ceil(self.infecter/self.people)
        self.zombies_out=math.ceil(self.zombies/self.people)
    def work_out_day_change_check(self):
        #秩序更改
        self.before_dead_zombies=self.dead_zombies
        if self.zombies+self.dead_people>1000:
            #开始减少,检测是否杀死1000丧尸
            if self.dead_zombies-self.before_dead_zombies>=1000:
                self.up_order()
                self.now_dead_zombies=self.dead_zombies
            else:
                self.sam_oder()
        #混乱
        if self.order in range(61,80):
            self.things=1
        elif self.order in range(51,60):
            self.things=2
        elif 0<self.order<50:
            self.things=3
        elif self.order<=0:
            self.things=4

    def yes_not_build_wall(self,day):
        if day==self.govement_speed:
            self.wall_build=1
    def up_order(self):
        add=random.randint(1,5)
        self.order+=add
    def sam_oder(self):
        sam=random.randint(10,30)
        self.order-=sam

    def infect_start(self):
        #判断是否有感染体
        if self.zombies!=1 or self.infecter!=1:
            #判断是否感染成功
            if self.check_out(self.infecter_out)==1:
                self.infecter=int((self.infecter+self.zombies)*self.R0)
                print("感染一次")
            else:
                print("感染失败")
                return
        else:
            print("没有感染源")
            return
    def break_day_start(self):
        #判断是否变成丧尸
        if self.check_out(self.dead_people_out)==1:
            self.zombies+=self.infecter
            self.infecter=0#全部感染
        else:#取一般感染
            self.zombies+=int(self.infecter/2)
            self.infecter=0
            self.dead_people+=int(self.infecter/2)


    def check_out(self,probability):#1 yes 0 no
        in_area=range(1,probability)
        out_area=random.randint(1,100)
        if out_area in in_area:
            return 1
        else:
            return 0