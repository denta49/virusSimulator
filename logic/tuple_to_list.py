from logic.get_element_from_tuple_to_list import get_element_from_tuple_to_list


def tuple_to_list(lst):
    for i in range(len(lst)):
        coordinates = get_element_from_tuple_to_list(lst, i)
        lst[i][0] = coordinates
