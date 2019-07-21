import matplotlib.pyplot as plt


def barplot_simple():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_count = [39, 117, 111, 110, 67, 29]
    plt.bar(year, tutorial_count)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()


def barplot_color():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_count = [39, 117, 111, 110, 67, 29]
    plt.bar(year, tutorial_count, color="#6c3376")

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()


def barplot_color2():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_count = [39, 117, 111, 110, 67, 29]
    plt.bar(year, tutorial_count, color="#6c3376", edgecolor="#409240", linewidth=2)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()


def barplot_color3():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_count = [39, 117, 111, 110, 67, 29]

    plt.bar(year[:-1], tutorial_count[:-1], color="#6c3376")
    plt.bar(year[-1], tutorial_count[-1], color="#6c3376", edgecolor="#409240", linewidth=2)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()


def barplot_horizontal():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_count = [39, 117, 111, 110, 67, 29]

    plt.barh(year[:-1], tutorial_count[:-1], color="#6c3376")
    plt.barh(year[-1], tutorial_count[-1], color="#6c3376", edgecolor="#409240", linewidth=2)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()
