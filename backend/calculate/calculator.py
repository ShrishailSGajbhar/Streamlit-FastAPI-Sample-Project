def perform_calculation(operation: str, number1: float, number2:float):
    '''
    Perform specified operation between two numbers

    Args:
        operation (str): ['Addition', "Subtraction", "Multiplication", "Division"]
        number1 (float): number1
        number2 (float): number2
    '''
    if operation=="Addition":
        return number1+number2
    elif operation=="Subtraction":
        return number1-number2
    elif operation=="Multiplication":
        return number1*number2
    elif operation=="Division":
        return number1/number2