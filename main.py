import player,map


def start_game():
    # 创建地图
    map_data = map.City()
    areas = map_data.rback()
    name = input("你的名字：")
    pa = player.Player(name, areas)
    print("你在城市:"+map_data.name+" 的地区： "+str(pa.area.number))

if __name__ == '__main__':
    file=open("data/text/main.txt","r")
    main_text=file.read()
    act=input(main_text)
    if act=="1":
        start_game()