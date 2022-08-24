import configparser

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


    decisition = input("Choose f if the arguments of the function are passed by a file, otherwise enter c letter: ")

    if decisition.lower() == 'f':
        with open('./arguments.ini') as fp:
            config = configparser.ConfigParser()
            config.read_file(fp)
            list_values = config.get('ARGS', 'VALUES')
            target_num = config.get('ARGS', 'TARGET')

        list_values = list_values.split(",")
        target_num = int(target_num)
        list_values = [int(str_value) for str_value in list_values]
        print(f"The values passed where {list_values}, {target_num}")
        find_integer_pair(list_values, target_num)
    elif decisition.lower() == 'c':
        list_values = input(""""Enter list of values as is showed in the nex example:\n
                                n_1,n_2,..,n_n:""")
        target_num = input("Type an integer value:")
        target_num = int(target_num)
        list_values = list_values.split(",")
        list_values = [int(str_value) for str_value in list_values]
        print(f"The values passed where {list_values}, {target_num}")
        find_integer_pair(list_values, target_num)
    else:
        print("neither f or c were typed")
