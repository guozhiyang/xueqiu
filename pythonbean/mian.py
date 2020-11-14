import sys
import os
#sys.path.append(r'C:\Users\61631\PycharmProjects\xueqiu\org.xy\pythonbean')
from pythonbean.combinationBean import Combination
from pythonbean.currentstockBean import currentstock
from pythonbean.rebalancestockBean import rebalancestock


module = sys.path;
for i in module:
    print(i)

# combinationBean = CombinationBean('123','lili','123123123','abc')
# combinationBean.eat()
# import pythonbean.combinationBean as pc

from pythonbean import *
combinationBean = Combination('123','lili','123123123','abc')
combinationBean.eat()
currentstockbean = currentstock('1029051','6.55','非银金融','10914318','中国平安')
combinationBean.csbs.append(currentstockbean)

for item in combinationBean.csbs:
    currentstockbean2 =  item
    currentstockbean2.print()


class  AAT:
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return super().__str__()