def ft_map(function_to_apply, list_of_inputs):
    result = []
    for elem in list_of_inputs:
        result.append(function_to_apply(elem))
    return (result)
