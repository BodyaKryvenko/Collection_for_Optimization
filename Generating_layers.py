def tuple_generator():
    result_list = []

    start_number = 8
    double_touple = (start_number, 5)
    result_list.append(start_number)
    result_list.append(double_touple)
    result_list.append((30, 5))

    while start_number < 256:
        start_number = start_number * 2
        result_list.append(start_number)
        double_touple = (start_number, 5)
        result_list.append(double_touple)

        second_layer_numb = start_number
        result_list.append((start_number, second_layer_numb, 5))
        while second_layer_numb < 256:
            second_layer_numb = second_layer_numb * 2
            result_list.append((start_number, second_layer_numb, 5))

            third_layer_numb = second_layer_numb
            result_list.append((start_number, second_layer_numb, third_layer_numb, 5))

            while third_layer_numb < 256:
                third_layer_numb = third_layer_numb * 2
                result_list.append((start_number, second_layer_numb, third_layer_numb, 5))

    return result_list


list_of_categories = tuple_generator()
