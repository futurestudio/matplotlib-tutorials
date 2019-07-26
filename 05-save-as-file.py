import matplotlib.pyplot as plt

year = [2014, 2015, 2016, 2017, 2018, 2019]
tutorial_count = [39, 117, 111, 110, 67, 29]


def save_as_pdf():
    plt.plot(year, tutorial_count, color="#6c3376", linewidth=3)
    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.savefig('line_plot.pdf')


def save_as_svg():
    plt.plot(year, tutorial_count, color="#6c3376", linewidth=3)
    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.savefig('line_plot.svg')


def save_as_png():
    plt.plot(year, tutorial_count, color="#6c3376", linewidth=3)
    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.savefig('line_plot.png')


def save_as_png_hq():
    plt.plot(year, tutorial_count, color="#6c3376", linewidth=3)
    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.savefig('line_plot_hq.png', dpi=300)


def save_as_png_hq_transparent():
    plt.plot(year, tutorial_count, color="#6c3376", linewidth=3)
    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    plt.savefig('line_plot_hq_transparent.png', dpi=300, transparent=True)


def save_as_jpg():
    plt.plot(year, tutorial_count, color="#6c3376", linewidth=3)
    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    # some options are only available for JPG
    plt.savefig('line_plot.jpg', dpi=300)


def save_as_jpg_optimize():
    plt.plot(year, tutorial_count, color="#6c3376", linewidth=3)
    plt.xlabel('Year')
    plt.ylabel('Number of futurestud.io Tutorials')

    # some options are only available for JPG
    plt.savefig('line_plot_optimized.jpg', dpi=300, quality=80, optimize=True, progressive=True)
