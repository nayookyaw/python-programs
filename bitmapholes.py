
class BitmapHoles:

    def __init__(self, str_input_list) -> None:
        self.str_input_list = str_input_list
    
    def bitmap_holes(self):
        two_d_list_array = []
        for input in self.str_input_list:
            # print (f"input : {input}")

            # convert string to list array
            input_list = list(input)
            # print (f"input list : {input_list}")
            two_d_list_array.append(input_list)

        count_of_zero = 0
        is_already_counted_two_d_list = []

        for i in range(len(two_d_list_array)):
            for j in range(len(two_d_list_array[i])):
                    # print (f"i : {i}, j : {j}, value : {two_d_list_array[i][j]}")
                    if (two_d_list_array[i][j] == '0'):
                        left_index = j - 1
                        right_index = j + 1
                        top_index = i - 1
                        bottom_index = i + 1

                        # check the index is valid or not or out of bound range
                        if (left_index >= 0):
                            if (two_d_list_array[i][left_index] == '0'):
                                if (i, left_index) not in is_already_counted_two_d_list:
                                    count_of_zero += 1

                                is_already_counted_two_d_list.append((i, left_index))
                                is_already_counted_two_d_list.append((left_index, i))
                                print (f"left_index : {left_index}, count_of_zero : {count_of_zero}")
                        
                        if (right_index >= 0):
                            if (two_d_list_array[i][right_index] == '0'):
                                if (i, right_index) not in is_already_counted_two_d_list:
                                    count_of_zero += 1

                                is_already_counted_two_d_list.append((i, right_index))
                                is_already_counted_two_d_list.append((right_index, i))
                                print (f"right_index : {right_index}, count_of_zero : {count_of_zero}")

                        if (top_index >= 0):
                            if (two_d_list_array[i][top_index] == '0'):
                                if (i, top_index) not in is_already_counted_two_d_list:
                                    count_of_zero += 1

                                is_already_counted_two_d_list.append((i, top_index))
                                is_already_counted_two_d_list.append((top_index, i))
                                print (f"top_index : {top_index}, count_of_zero : {count_of_zero}")
                        
                        if (bottom_index >= 0):
                            if (two_d_list_array[i][bottom_index] == '0'):
                                if (i, bottom_index) not in is_already_counted_two_d_list:
                                    count_of_zero += 1

                                is_already_counted_two_d_list.append((i, bottom_index))
                                is_already_counted_two_d_list.append((bottom_index, i))
                                print (f"bottom_index : {bottom_index}, count_of_zero : {count_of_zero}")

        return count_of_zero

bitmapHole = BitmapHoles(["10111", "10101", "11101", "11111"])
# bitmapHole = BitmapHoles(['0000', '0000'])
print (f"{bitmapHole.bitmap_holes()} holes found")


# 1 0 1 1 1
# 1 0 1 0 1
# 1 1 1 0 1
# 1 1 1 1 1