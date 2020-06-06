def ft_reduce(function_to_apply, list_of_inputs):
    if (not isinstance(list_of_inputs, list)):
        raise TypeError('ft_reduce() arg 2 must support iteration')
    if (len(list_of_inputs) == 0):
        raise TypeError("reduce() of empty sequence with no initial value")
    if (len(list_of_inputs) == 1):
        return (list_of_inputs[0])
    if not (str(type(function_to_apply)) == "<class 'function'>"):
        raise TypeError(str(type(function_to_apply))[7:-1:] + " object is not callable")
    temp = list_of_inputs[0]
    for i in range(len(list_of_inputs) - 1):
        temp = function_to_apply(temp, list_of_inputs[i + 1])
    return (temp)
