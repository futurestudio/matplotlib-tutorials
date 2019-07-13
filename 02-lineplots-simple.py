import matplotlib.pyplot as plt


def lineplot_simple():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_count = [39, 117, 111, 110, 67, 29]
    plt.plot(year, tutorial_count)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()


def lineplot_color():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_count = [39, 117, 111, 110, 67, 29]
    plt.plot(year, tutorial_count, color="#6c3376", linewidth=3)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()


def lineplot_color2():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_public = [39, 117, 98, 54, 28, 15]
    tutorial_premium = [0, 0, 13, 56, 39, 14]
    plt.plot(year, tutorial_public, color="#6c3376", linewidth=3)
    plt.plot(year, tutorial_premium, color="#f3e151", linewidth=3)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()
