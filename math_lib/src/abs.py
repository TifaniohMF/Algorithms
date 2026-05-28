'''
In this program, I write the absolute value 
For a number
>> abs(-34) == 34

To find a max absolute value in a list
>> absMax([1,2,3,-12]) == 12

To find a min absolute value in a list
>> absMin([-1,2,3,-12]) == 1
'''

class absolute:
    def __init__(self, data):
        self.number = data if isinstance(data, (int, float)) else None
        self.liste= data if isinstance(data, list) else []

    def abs(self):
        if self.number > 0:
            return self.number
        else:
            return -self.number

    def absMax(self):
        j = self.liste[0]
        for i in self.liste:
            if absolute(i).abs() > absolute(j).abs():
                j = absolute(i).abs()
        return j

    def absMin(self):
        j = self.liste[0]
        for i in self.liste:
            if absolute(i).abs() < absolute(j).abs():
                j = absolute(i).abs()
        return j
