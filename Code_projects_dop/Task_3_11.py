import re
import matplotlib.pyplot as plt


def get_src():
    f = open('src.txt', 'r', encoding='utf-8')
    res = f.read()
    src = re.findall(r';"\d+"', res)
    for i in range(len(src)):
        src[i] = src[i][2:-1]
    src = tuple(sorted(src))
    return src


def get_srce():
    f = open('src.txt', 'r', encoding='utf-8')
    res = f.read()
    srce = re.findall(r';"\w+";', res)
    for i in range(len(srce)):
        srce[i] = srce[i][2:-2]
    srce = tuple(sorted(srce))
    return srce


def get_counters(src):
    b = {}
    c = 1
    for i in range(len(src) - 1):
        if src[i] == src[i + 1]:
            c += 1
        else:
            b[src[i]] = c
            c = 1
    return b


def get_counters_genre(src):
    b = {}
    c = 1
    for i in range(len(src) - 1):
        if src[i] == src[i + 1]:
            c += 1
        else:
            b[src[i]] = c
            c = 1
    return b


def draw_plot_bar(b):
    names = list(b.keys())
    amount = list(b.values())
    plt.bar(names, amount)
    plt.show()


def draw_plot_pie(b):
    names = list(b.keys())
    year = list(b.values())
    plt.pie(year, labels=names)
    plt.show()

draw_plot_pie(get_counters_genre(get_srce()))