def ft_filter(function_to_apply, list_of_inputs):
    result = []
    for elem in list_of_inputs:
        if function_to_apply(elem) == 1:
            result.append(elem)
    return (result)
