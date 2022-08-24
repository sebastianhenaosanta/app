def find_integer_pair(list_of_ints, num):

    list_of_ints = sorted(list_of_ints)

    (low_index, high_index) = (0, len(list_of_ints)-1)

    while low_index < high_index:

        if list_of_ints[low_index] + list_of_ints[high_index] == num:
            print(f"{list_of_ints[high_index]},{list_of_ints[low_index]}")
        if list_of_ints[low_index] + list_of_ints[high_index] < num:
            low_index += 1
        else:
            high_index -= 1




if __name__ == "__main__":

    int_lst = [1,9,5,0,20,-4,12,16,7]
    number = 12
    find_integer_pair(int_lst, number)