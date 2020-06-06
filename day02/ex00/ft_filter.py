def ft_filter(function_to_apply, list_of_inputs):
    if not isinstance(list_of_inputs, list):
        raise TypeError(str(type(list_of_inputs))[7:-1:] + " object is not callable")
    if not (str(type(function_to_apply)) == "<class 'function'>"):
        raise TypeError(str(type(function_to_apply))[7:-1:] + " object is not callable")
    result = []
    for elem in list_of_inputs:
        if function_to_apply(elem) == True:
            result.append(elem)
    return (result)
