#!/usr/bin/python3
'''
伪代码：
1、打印游戏的任务
2、创建一个木屋的列表
3、在5个木屋中随机分配敌人、同伴或者空闲
4、提示选择一个木屋的编号
5、如果选中敌人占据的木屋，则打印“你输了”
6、否则，打印“你赢了”

'''

import random
import textwrap

if __name__ == '__main__' :
    keep_playing = 'y'
    width = 72
    occupants = ['enemy', 'friend', 'unoccupied']  # 木屋占有人的类型
    dotted_line = '-' * width

    print(dotted_line)
    print("Attack of The Orcs v0.0.1\n")  # \033[1m:以粗体显示字符  \033[0m:返回正常的打印样式
    msg = ("The War between humans and their arch enemies, Orcs, was in the "
           "offing. Sir Foo, one of the brave knights guarding the southern"
           "plains began a long joureny towards the east throught an unknown"
           "dense forest .On this way, he spotted a small islated settlement."
           "Tired and hoping to replenish his food stock, he decided to take"
           "a dector. As he apporached the village, he saw five huts. There "
           "was no one to be seen around. Hesitantly, he decided to enter...")
    print(textwrap.fill(msg, width=width))

    print("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print("TIP:")
    print("\tBe careful as there are enemies lurking around!")
    print(dotted_line)


    while keep_playing == 'y':
        huts = []
        # Randomly append 'enemy' or 'friend' or None to the huts list
        while len(huts) < 5:
            computer_choice = random.choice(occupants)
            huts.append(computer_choice)

        # Prompt user t oselect a hut
        msg = "Choose a hut number to enter(1,5)"
        user_choice = input("\n" + msg)
        idx = int(user_choice)

        # Print the occupant info
        print("Revealing the occupants...")
        msg = ""
        for i in range(len(huts)):
            occupant_info = "<%d:%s>" % (i + 1, huts[i])
            if i + 1 == idx:
                occupant_info = occupant_info
            msg += occupant_info
        print("\t" + msg)
        print(dotted_line)
        print("Entering hut %d ..." % idx)

        # Determing and announce the winner
        if huts[idx - 1] == 'enemy':
            print("You Lose....(Better luck next time!)")
        else:
            print("Congratulations! You Win!")

        print(dotted_line)
        keep_playing = input("Playing again? YES(y)/NO(n)")

