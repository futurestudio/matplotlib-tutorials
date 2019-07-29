import matplotlib.pyplot as plt


def labels_simple():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_public = [39, 117, 98, 54, 28, 15]
    tutorial_premium = [0, 0, 13, 56, 39, 14]
    plt.plot(year, tutorial_public, color="#6c3376", linewidth=3)
    plt.plot(year, tutorial_premium, color="#f3e151", linewidth=3)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.show()


def labels_font():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_public = [39, 117, 98, 54, 28, 15]
    tutorial_premium = [0, 0, 13, 56, 39, 14]
    plt.plot(year, tutorial_public, color="#6c3376", linewidth=3)
    plt.plot(year, tutorial_premium, color="#f3e151", linewidth=3)

    plt.xlabel('Year', color='blue', family='serif', fontsize=50)
    plt.ylabel('Number of futurestud.io Tutorials', fontsize='small')

    plt.show()


def labels_background():
    year = [2014, 2015, 2016, 2017, 2018, 2019]
    tutorial_public = [39, 117, 98, 54, 28, 15]
    tutorial_premium = [0, 0, 13, 56, 39, 14]
    plt.plot(year, tutorial_public, color="#6c3376", linewidth=3)
    plt.plot(year, tutorial_premium, color="#f3e151", linewidth=3)

    plt.xlabel('Year', color='blue', family='serif', fontsize=50)
    plt.ylabel('Number of futurestud.io Tutorials', backgroundcolor='red', fontsize='small')

    plt.show()


labels_simple()
labels_font()
labels_background()
