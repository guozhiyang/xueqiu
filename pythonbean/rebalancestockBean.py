class rebalancestock:
    '一个组合对象'

    def __init__(self,id,rebalancing_id,stock_id,stock_name,rb_value,stock_symbol,volume,price,net_value,weight,target_weight,prev_weight,prev_target_weight,prev_weight_adjusted,prev_volume,prev_price,prev_net_value,proactive,created_at,updated_at,target_volume,prev_target_volume):
        self.id = id #递增ID，无实际含义
        self.rebalancing_id = rebalancing_id #此次调整ID
        self.stock_id = stock_id #股票ID
        self.stock_name = stock_name #股票名称
        self.rb_value = rb_value  # 调整的具体值  --  单独自己添加的属性
        self.stock_symbol = stock_symbol #股票代码
        self.volume = volume #成交量
        self.price = price #参考成交价
        self.net_value = net_value #净值？
        self.weight = weight #调整后的仓位百分比
        self.target_weight = target_weight #目前仓位百分比
        self.prev_weight = prev_weight #先前的仓位百分比
        self.prev_target_weight = prev_target_weight #先前的目标百分比
        self.prev_weight_adjusted = prev_weight_adjusted #当前的百分占比情况。   即实际的仓位值
        self.prev_volume = prev_volume #先前体积，意思没懂
        self.prev_price = prev_price #先前成交价格？
        self.prev_net_value = prev_net_value #网络价格？
        self.proactive = proactive #积极
        self.created_at = created_at #创建时间
        self.updated_at = updated_at #更新时间
        self.target_volume = target_volume #目标体积？
        self.prev_target_volume = prev_target_volume #先前目标体积


    def myprint(self):
        print(' stock_id = ' + self.stock_id +
              ' ,stock_name = ' + self.stock_name)
