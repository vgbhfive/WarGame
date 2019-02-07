import random

from wargame.abstractgameunit import GameUnitError
from wargame.gameutils import print_dotted
from wargame.hut import Hut
from wargame.knight import Knight
from wargame.orcrider import OrcRider


# 游戏类
class AttackOfTheOrcs:
    def __init__(self):
        self.huts = [] # 创建一个hut类的实例表
        self.player = None # 实例化player

    # 获取木屋的占据信息
    def get_occupants(self):
        return [x.get_occupant_type() for x in self.huts]

    # 展示游戏任务
    def show_game_mission(self):
        print("Mission:")
        print("\t1. fight with the enemy!")
        print("TIP:")
        print("\tbring all the huts in the villege under your control")
        print_dotted()

    # 确认用户的选择
    def _process_user_choice(self):
        verify_choice = True
        idx = 0
        print("Current occupant: %s" % self.get_occupants())

        while verify_choice:
            user_choice = input("Choose a number to enter (1-5):")
            try:
                idx = int(user_choice)
            except GameUnitError as e: # 异常ValueError
                print("Invalid input: %s" % e.args)
                continue
            try:
                if self.huts[idx-1].is_acquire:
                    print("You have try again!")
                else:
                    verify_choice = False
            except IndexError: # 异常IndexError
                print("Invalid input:", idx)
                print("Number should be in the range 1 - 5, Please try again.")
                continue
        return idx

    # hut类的实例化和分配(占据木屋)
    def occupy_huts(self):
        occupants = ['enemy', 'friend', None]  # 木屋占有人的类型
        # Randomly append 'enemy' or 'friend' or None to the huts list
        for i in range(5):
            computer_choice  = random.choice(occupants)
            if computer_choice == 'enemy':
                name  = 'enemy-' + str(i+1)
                self.huts.append(Hut(i+1, OrcRider(name)))
            elif computer_choice == 'friend':
                name = 'friend-' + str(i+1)
                self.huts.append(Hut(i+1, Knight(name)))
            else:
                self.huts.append(Hut(i+1, computer_choice))

    # 开始游戏
    def play(self):
        self.player = Knight()
        self.occupy_huts()
        # 确认木屋全部检查过
        acquire_hut_count = 0

        # 游戏人物及人物血量
        self.show_game_mission()
        self.player.show_health(bold=True)

        # 开始War
        while acquire_hut_count < 5:
            # 玩家选择攻占的木屋
            idx = self._process_user_choice()
            # 开始占据木屋
            self.player.acquire_hut(self.huts[idx-1])

            # 结束条件
            if self.player.health_meter <= 0:
                print("You Lose, Better luck next time!")
                break

            if self.huts[idx-1].is_acquire:
                acquire_hut_count += 1

        if acquire_hut_count == 5:
            print("Congratulation for you! You Win!!!")

