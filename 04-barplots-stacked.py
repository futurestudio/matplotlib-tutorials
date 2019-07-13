import matplotlib.pyplot as plt


def barplot_stacked_simple():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_public = [39, 117, 98, 54, 28, 15]
    tutorial_premium = [0, 0, 13, 56, 39, 14]

    plt.bar(year, tutorial_public, color="#6c3376")
    plt.bar(year, tutorial_premium, bottom=tutorial_public, color="#f3e151")

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()


def barplot_stacked_reversed():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_public = [39, 117, 98, 54, 28, 15]
    tutorial_premium = [0, 0, 13, 56, 39, 14]

    plt.bar(year, tutorial_premium, color="#f3e151")
    plt.bar(year, tutorial_public, bottom=tutorial_premium, color="#6c3376")

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()


def barplot_stacked_horizontal():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_public = [39, 117, 98, 54, 28, 15]
    tutorial_premium = [0, 0, 13, 56, 39, 14]

    plt.barh(year, tutorial_premium, color="#f3e151")
    # notice bottom became left
    plt.barh(year, tutorial_public, left=tutorial_premium, color="#6c3376")

    plt.xlabel('Number of futurestud.io Tutorials')
    plt.ylabel('Year')

    plt.show()
