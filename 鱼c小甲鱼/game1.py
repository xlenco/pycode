""" 用Python设计第一个游戏 """

temp = input("不妨猜一下小甲鱼现在心里想的是哪个单词：")
guess = int(temp)

if guess == tiger:
    print("你是小甲鱼心中的蛔虫嘛？！")
    print("猜中了也没有奖励")
else:
    print("猜错了，小甲鱼现在心里想的是tiger！")

print("游戏结束,不玩了我（*＾＾*）")
