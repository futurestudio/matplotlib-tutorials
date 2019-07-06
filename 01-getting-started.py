import matplotlib.pyplot as plt


def simple_plot():
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 4, 9, 16]

    plt.plot(x, y)
    plt.show()


def scatter_plot():
    x = [0, 1, 2, 5, 8]
    y = [1, 4, 3, 2, 5]
    plt.scatter(x, y)
    plt.show()


def scatter_plot_custom_design():
    x = [0, 1, 2, 5, 8]
    y = [1, 4, 3, 2, 5]
    plt.scatter(x, y, color='red')
    plt.show()

    x = [0, 1, 2, 5, 8]
    y = [1, 4, 3, 2, 5]
    plt.scatter(x, y, color='red', marker='^')
    plt.show()


def scatter_plot_labels():
    x = [0, 1, 2, 5, 8]
    y = [1, 4, 3, 2, 5]
    plt.scatter(x, y, color='red', marker='^')
    plt.xlabel('X Axis Label')
    plt.ylabel('Y Axis Label')
    plt.show()


def scatter_plot_limits():
    x = [0, 1, 2, 5, 8]
    y = [1, 4, 3, 2, 5]
    plt.scatter(x, y, color='red', marker='^')
    plt.xlabel('X Axis Label')
    plt.ylabel('Y Axis Label')
    plt.ylim(0)
    plt.show()

scatter_plot_custom_design()