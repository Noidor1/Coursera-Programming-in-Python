class Value:
    
    def __init__(self, amount=None):
        self.amount = amount
        
    @staticmethod
    def _prepare_value(value, commission):
        return value * (1-commission)
        
    def __get__(self, obj, obj_type):
        return self.amount
    
    def __set__(self, obj, value):
        self.amount = self._prepare_value(value, obj.commission)
    
class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission