from wargame.abstractgameunit import AbstractGameUnit


# 人类骑士
class Knight(AbstractGameUnit):
    def __init__(self, name='Sir Foo'):
        super().__init__(name)
        self.health_meter = 40
        self.unit_type = 'Friend'

    def info(self):
       print("I`m a Knight!")

    # 攻击木屋
    def acquire_hut(self, hut):
        print("Entering hut %d \n" % hut.number, end=' ')
        is_enemy = (isinstance(hut.occupant, AbstractGameUnit) and hut.occupant.unit_type == 'enemy') # 判断木屋中是否为enemy
        continue_attack = 'y'

        if is_enemy:
            print("Enemy sighted!")
            self.info()
            hut.occupant.info() # 全部木屋属性
            while continue_attack:
                continue_attack = input(".....continue attack? (y/n):")
                if (continue_attack == 'n'):
                    self.run_away() # 逃跑，恢复血量
                    break

                self.attack(hut.occupant) # 攻击对方

                if hut.occupant.health_meter <= 0:
                    print("")
                    hut.acquire(self) # 占据木屋
                    break
                if self.health_meter <= 0:
                    print("") # Lose
                    break
        else:
            if hut.get_occupant_type() == 'unacquired!':
                print("Hut is unoccupantied")
            else:
                print("Friend sighted!")
            hut.acquire(self) # 占据木屋
            self.heal() # 休息回血



