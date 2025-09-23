
class AscendingOrder:

    def __init__(self, input_list):
        self.input_list = input_list
    
    def ascending_order(self):
        # return sorted(self.input_list)
        sorted_list = []
        un_sorted_list = self.input_list.copy()
        temp_min = self.input_list[0] if len(self.input_list) > 0 else None
        
        for item in self.input_list:
            temp_min = un_sorted_list[0]
            for input in un_sorted_list:
                if (temp_min > input):
                    temp_min = input
            
            sorted_list.append(temp_min)
            un_sorted_list.remove(temp_min)
        
        return sorted_list

ascendingOrder = AscendingOrder([34, 2, 23, 67, 4, 89])
print (f"Original List: {ascendingOrder.input_list}")
print (f"Sorted List in Ascending Order: {ascendingOrder.ascending_order()}")