import random

# 打印隔行符
def print_dotted (width=72) :
    dotted_line = '-' * width
    print(dotted_line)

# 游戏公有
class GameUnit:
    def __init__(self, name):
        self.name = name
        self.health_meter = 0
        self.enemy = ''
        self.unit_type = ''

    def info(self):
        pass

    def attack(self, enemy):
        hit_list = 4 * ['player'] + 6 * ['enemy']
        injured_unit = random.choice(hit_list)
        hit_point = self.health_meter
        injury = random.randint(5, 15)
        self.health_meter = max(hit_point - injury, 0)
        print("ATTACK!")
        self.show_health(end=' ')
        enemy.show_health(end=' ')

    # 治疗(骑士)
    def heal(self):
        self.health_meter = 40

    def run_away(self):
        print("I`m running!\n I will be coming ,Wait for me!")
        print_dotted()

    def show_health(self, bold=False, end='\n'):
        msg = "Health: %s: %d" % (self.name, self.health_meter)

        if bold:
            print(msg, end=end)
        else:
            print(msg, end=end)

# 兽人
class OrcRider(GameUnit):
    def __init__(self, name='Enemy'):
        super().__init__(name)
        self.health_meter = 30
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        print("Grrrr..I am an Orc Wolf Rider. Don't mess with me.")

# 人类骑士
class Knight(GameUnit):
    def __init__(self, name='Sir Foo'):
        super().__init__(name)
        self.health_meter = 40
        self.unit_type = 'Friend'

    def info(self):
       print("I`m a Knight!")

    # 攻击木屋
    def acquire_hut(self, hut):
        print("Entering hut %d \n" % hut.number, end=' ')
        is_enemy = (isinstance(hut.occupant, GameUnit) and hut.occupant.unit_type == 'enemy')
        continue_attack = 'y'

        if is_enemy:
            print("Enemy sighted!")
            self.info()
            hut.occupant.info()
            while continue_attack:
                continue_attack = input(".....continue attack? (y/n):")
                if (continue_attack == 'n'):
                    self.run_away()
                    break

                self.attack(hut.occupant)

                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire()
                    break
                if self.health_meter <= 0:
                    print("")
                    break
        else:
            if hut.get_occupant_type() == 'unacquired!':
                print("Hut is unoccupantied")
            else:
                print("Friend sighted!")
            hut.acquire(self)
            self.heal()

# 木屋类
class Hut:
    def __init__(self, number, occupant):
        self.number = number
        self.occupant = occupant
        self.is_acquire = False

    # 获取信息
    def acquire(self, new_occupant):
        self.occupant = new_occupant
        self.is_acquire = True
        print("Good Job! Hut %d acquired!" % self.number)

    def get_occupant_type(self):
        if self.is_acquire:
            occupant_type = 'acquired!'
        elif self.occupant is None:
            occupant_type = 'unacquired'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type

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
            user_choice = input("Choose a number to neter (1-5):")
            idx = int(user_choice)
            if self.huts[idx-1].is_acquire:
                print("You have try again!")
            else:
                verify_choice = False
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

        self.show_game_mission()
        self.player.show_health(bold=True)

        while acquire_hut_count < 5:
            idx = self._process_user_choice()
            self.player.acquire_hut(self.huts[idx-1])

            if self.player.health_meter <= 0:
                print("You Lose, Better luck next time!")
                break

            if self.huts[idx-1].is_acquire:
                acquire_hut_count += 1

        if acquire_hut_count == 5:
            print("Congratulation for you! You Win!!!")

if __name__ == '__main__':
    game = AttackOfTheOrcs()
    game.play()