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

def print_dotted (width=72) :
    dotted_line = '-' * width
    print(dotted_line)

def show_theme_message (width) :
    print_dotted()
    print("Attack of The Orcs v0.0.1\n")  # \033[1m:以粗体显示字符  \033[0m:返回正常的打印样式

    msg = ("The War between humans and their arch enemies, Orcs, was in the "
           "offing. Sir Foo, one of the brave knights guarding the southern"
           "plains began a long joureny towards the east throught an unknown"
           "dense forest .On this way, he spotted a small islated settlement."
           "Tired and hoping to replenish his food stock, he decided to take"
           "a dector. As he apporached the village, he saw five huts. There "
           "was no one to be seen around. Hesitantly, he decided to enter...")
    print(textwrap.fill(msg, width=width))

def show_game_mission () :
    print("Mission:")
    print("\tChoose a hut where Sir Foo can rest...")
    print("TIP:")
    print("\tBe careful as there are enemies lurking around!")
    print_dotted()

def occupy_huts () :
    occupants = ['enemy', 'friend', 'unoccupied']  # 木屋占有人的类型

    huts = []
    # Randomly append 'enemy' or 'friend' or None to the huts list
    while len(huts) < 5:
        computer_choice = random.choice(occupants)
        huts.append(computer_choice)

    return huts

def process_user_choices () :
    # Prompt user t oselect a hut
    msg = "Choose a hut number to enter(1,5)"
    user_choice = input("\n" + msg)
    idx = int(user_choice)
    return idx

def reveal_occupants (idx, huts) :
    # Print the occupant info
    print("Revealing the occupants...")
    msg = ""
    for i in range(len(huts)):
        occupant_info = "<%d:%s>" % (i + 1, huts[i])
        if i + 1 == idx:
            occupant_info = occupant_info
        msg += occupant_info
    print("\t" + msg)
    print_dotted()
    print("Entering hut %d ..." % idx , end=' ')

def reset_health_meter (health_meter) :
    '''
    Top level control function for running the application
    :param health_meter:
    :return:
    '''
    health_meter["player"] = 40
    health_meter["enemy"] = 30

def show_health (health_meter) :
    print("Health: Sir Foo: %d  Enemy: %d" % (health_meter['player'] , health_meter['enemy']))

def attack (health_meter) :
    hit_list = 4*['player'] + 6 * ['enemy']
    injured_unit = random.choice(hit_list)
    hit_point = health_meter[injured_unit]
    injury = random.randint(10, 15)
    health_meter[injured_unit] = max(hit_point - injury , 0)
    print("ATTACK!")
    show_health(health_meter)

def play_game (health_meter) :
    # huts
    huts = occupy_huts()
    # input idx
    idx = process_user_choices()
    # output huts
    reveal_occupants(idx, huts)

    # Determing and announce the winner
    if huts[idx - 1] == 'enemy':
        print("\nENEMY FIGHT!!!")
        show_health(health_meter)
        continue_attack = True

        while continue_attack :
            continue_attack = input("-----Continue Attack YES(y)NO(n):")
            if continue_attack == 'n':
                print("RUNNING AWAY with the following health status......")
                show_health(health_meter)
                print("GAME OVER!")
                break

            attack(health_meter)

            if health_meter['enemy'] <= 0:
                print("Congratulations! You Win!")
                break
            if health_meter['player'] <= 0:
                print("You Lose!")
                break
    else:
        print("Congratulations! You Win!")
    print_dotted()

def run_application ():
    keep_playing = 'y'
    width = 72
    dotted_line = '-' * width

    health_meter = {}
    reset_health_meter(health_meter)

    # show message
    show_theme_message(width)

    # show mission
    show_game_mission()

    while keep_playing == 'y':
        reset_health_meter(health_meter)
        play_game(health_meter)
        keep_playing = input("Playing again? YES(y)/NO(n)")

if __name__ == '__main__' :
    run_application()


