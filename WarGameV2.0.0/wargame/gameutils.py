import random
from abc import abstractmethod


# 打印隔行符
def print_dotted (width=72) :
    dotted_line = '-' * width
    print(dotted_line)

# 确定受伤方向
def weighted_random_selection(obj1, obj2):
    """
    Randomly select between two objects based on assigned 'weight'
    """
    weighted_list = 4 * [id(obj1)] + 6 * [id(obj2)]
    selection = random.choice(weighted_list)

    if selection == id(obj1): # 判断选择，然后返回对象
        return obj1

    return obj2
