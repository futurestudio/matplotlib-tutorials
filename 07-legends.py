import matplotlib.pyplot as plt

year = [2014, 2015, 2016, 2017, 2018, 2019]
tutorial_public = [39, 117, 98, 54, 28, 15]
tutorial_premium = [0, 0, 13, 56, 39, 14]


def legends_fail():
    plt.plot(year, tutorial_public, color="#6c3376", linewidth=3)
    plt.plot(year, tutorial_premium, color="#f3e151", linewidth=3)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.legend()

    plt.show()


def legends_simple():
    plt.plot(year, tutorial_public, label='Public Tutorials', color="#6c3376", linewidth=3)
    plt.plot(year, tutorial_premium, label='Premium Tutorials', color="#f3e151", linewidth=3)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.legend()

    plt.show()


def legends_alternative():
    public, = plt.plot(year, tutorial_public, color="#6c3376", linewidth=3)
    premium, = plt.plot(year, tutorial_premium, color="#f3e151", linewidth=3)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.legend([public, premium], ['Public Tutorials', 'Premium Tutorials'])

    plt.show()


def legends_custom():
    plt.plot(year, tutorial_public, label='Public Tutorials', color="#6c3376", linewidth=3)
    plt.plot(year, tutorial_premium, label='Premium Tutorials', color="#f3e151", linewidth=3)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.legend(loc='upper left', ncol=2)

    plt.show()


def legends_custom2():
    plt.plot(year, tutorial_public, label='Public Tutorials', color="#6c3376", linewidth=3)
    plt.plot(year, tutorial_premium, label='Premium Tutorials', color="#f3e151", linewidth=3)

    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.legend(loc='upper right', title='Cool Legend', frameon=False, fontsize='large')

    plt.show()
