

class FindMaxValue:
    def __init__(self, input_list) -> None:
        self.input_list = input_list
    
    def find_max(self):
        print ("Finding maximum value...")
        print (f"input list : {self.input_list}")

        temp_max = self.input_list[0] if len(self.input_list) > 0 else 0

        for input in self.input_list:
            print (f"current input : {input}")
            if input > temp_max:
                temp_max = input

        return temp_max
    

findMaxValue = FindMaxValue([-1, -2, -3, -4, -5, 0])
print (findMaxValue.find_max())