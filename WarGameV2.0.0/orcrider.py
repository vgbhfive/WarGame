from abstractgameunit import AbstractGameUnit


# 兽人
class OrcRider(AbstractGameUnit):
    def __init__(self, name='Enemy'):
        super().__init__(name)
        self.health_meter = 30
        self.unit_type = 'enemy'
        self.hut_number = 0

    def info(self):
        print("Grrrr..I am an Orc Wolf Rider. Don't mess with me.")
