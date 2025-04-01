def apply_conditional_formatting(cell_value, condition):
    if condition(cell_value):
        return "Highlighted"
    return "Normal"