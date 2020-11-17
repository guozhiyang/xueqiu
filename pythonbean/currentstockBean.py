class currentstock:
    '当前在仓的仓位情况'

    def __init__(self,stock_id, weight, segment_name, segment_id, stock_name):
        self.stock_id = stock_id
        self.weight = weight
        self.segment_name = segment_name
        self.segment_id = segment_id
        self.stock_name = stock_name

    def myprint(self):
        print(' stock_id = ' + self.stock_id +
              ' ,weight = ' + self.weight +
              ' ,segment_name = ' + self.segment_name +
              ' ,segment_id = ' + self.segment_id +
              ' ,stock_name = ' + self.stock_name)