import matplotlib.pyplot as plt

def plot(data_list, file_name):
    plt.clf()
    x = list(range(len(data_list[0])))

    for data in data_list:
        plt.plot(x, data)

    plt.savefig("{}.png".format(file_name))


def plot_with_dots(data_list, buy_dots, sell_dots, file_name):
    plt.clf()
    x = list(range(len(data_list[0])))

    for data in data_list:
        plt.plot(x, data)

    for data in buy_dots:
        plt.plot(data[0], data[1], marker="^", markersize=10, color='b')

    for data in sell_dots:
        plt.plot(data[0], data[1], marker="v", markersize=10, color='r')

    plt.savefig("{}.png".format(file_name))