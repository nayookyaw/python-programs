
class DescendingOrder:

    def __init__(self, input_list) -> None:
        self.input_list = input_list
    
    def descending_order(self):
        # return sorted(self.input_list, reverse=True)
        
        sorted_list = []
        un_sorted_list = self.input_list.copy()

        for i in range(len(self.input_list)):
            
            temp_max = un_sorted_list[0]
            for input in un_sorted_list:
                if (input > temp_max):
                    temp_max = input
            
            sorted_list.append(temp_max)
            un_sorted_list.remove(temp_max)
        return sorted_list

descendingOrder = DescendingOrder([34, 2, 23, 67, 4, -89])
print (f"Original List: {descendingOrder.input_list}")
print (f"Sorted List in Descending Order: {descendingOrder.descending_order()}")