import matplotlib.pyplot as plt

def build_bar_chart(data):
    """
    Строит столбчатую диаграмму на основе данных.

    Args:
        data (dict): Словарь, где ключи — категории, значения — числа.
    """
    categories = list(data.keys())
    values = list(data.values())
    plt.bar(categories, values)
    plt.show()