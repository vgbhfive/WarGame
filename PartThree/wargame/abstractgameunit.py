import random
from abc import abstractmethod

from wargame.gameutils import print_dotted, weighted_random_selection


# 异常处理
class GameUnitError(Exception):
    def __init__(self, messgae="", code =000):
        super().__init__(messgae)
        self.error_messgae = '~' * 50 + '\n'
        self.error_dict = {
            000: "ERROR_000: Unspecified Error!",
            101: "ERROR_101: Health Meter Problem!",
            102: "ERROR_102: Attack issue! Ignored.",
            103: "ERROR_103: Input Value Error!",
            104: "ERROR_104: Index Error, Number should be in the range 1 - 5, Please try again."
        }
        try:
            self.error_messgae += self.error_dict[code]
        except:
            self.error_messgae += self.error_dict[000]
        self.error_messgae += '\n' + '~'*50

# 游戏公有
class AbstractGameUnit:
    def __init__(self, name):
        self.name = name
        self.health_meter = 0
        self.enemy = ''
        self.unit_type = ''

    @abstractmethod
    def info(self):
        pass

    # 攻击对方
    def attack(self, enemy):
        injured_unit = weighted_random_selection(self, enemy) # 选择受伤方向
        injury = random.randint(5, 15) # 所受伤害
        injured_unit.health_meter = max(injured_unit.health_meter - injury, 0) # 减少血量
        print("ATTACK!")
        self.show_health(end=' ')
        enemy.show_health(end=' ')

    # 治疗(骑士)
    def heal(self):
        self.health_meter = 40

    # 逃跑，治疗
    def run_away(self):
        print("I`m running!\n I will be coming ,Wait for me!")
        print_dotted()

    # 展示血量
    def show_health(self, bold=False, end='\n'):
        msg = "Health: %s: %d" % (self.name, self.health_meter)
        if bold:
            print(msg, end=end)
        else:
            print(msg, end=end)

