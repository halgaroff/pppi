import matplotlib.pyplot as plt

def build_bar_chart(data):
    categories = list(data.keys())
    values = list(data.values())
    plt.bar(categories, values)
    plt.show()