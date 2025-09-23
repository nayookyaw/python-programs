

class FindMinValue:

    def __init__(self, input_list) -> None:
        self.input_list = input_list

    def find_min_value(self):
        temp_min = self.input_list[0] if len(self.input_list) > 0 else 0
        for input in range(len(self.input_list)):
            # print (self.input_list[input])
            if self.input_list[input] < temp_min:
                temp_min = self.input_list[input]

        return temp_min

findMinValue = FindMinValue([3, 5, 1, 8, -2, -7])
print (f"result : {findMinValue.find_min_value()}")