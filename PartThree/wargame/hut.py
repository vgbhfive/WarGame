

# 木屋类
class Hut:
    def __init__(self, number, occupant):
        self.number = number # 编号
        self.occupant = occupant # 占据属性
        self.is_acquire = False # 是否占据

    # 木屋已占据
    def acquire(self, new_occupant):
        self.occupant = new_occupant
        self.is_acquire = True
        print("Good Job! Hut %d acquired!" % self.number)

    # 获取当前木屋的占据属性
    def get_occupant_type(self):
        if self.is_acquire:
            occupant_type = 'acquired!'
        elif self.occupant is None:
            occupant_type = 'unacquired'
        else:
            occupant_type = self.occupant.unit_type

        return occupant_type