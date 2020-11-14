class Combination:
    '一个组合对象'

    def __init__(self,id,name,symbol,owner_id):
        super
        self.id = id
        self.name = name
        self.symbol = symbol
        self.owner_id = owner_id
        self.csbs = []
        self.rsbs = []

    def __str__(self) -> str:
        return super().__str__()

    def myprint(self):
        print( ' id = ' + self.id +
               ' ,name = ' + self.name +
               ' ,symbol = ' + self.symbol +
               ' ,owner_id = ' + self.owner_id)

    def eat(self):
        print('123123123')


combinationBean = Combination('123','lili','123123123','abc')
combinationBean.eat()