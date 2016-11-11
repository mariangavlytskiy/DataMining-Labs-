import re
from matplotlib import pyplot as plt


def count_words_data(words):
    counted_words = {}
    for w in words:
        w = w[:int(len(w) * 0.75)]
        if w not in counted_words:
            counted_words[w] = 0
        counted_words[w] += 1
    return counted_words

def normailized_text():
    text = []
    with open('text.txt', 'r') as inp:
        for line in inp:
            text.extend(re.sub('[^\w]+', ' ', line).lower().strip().split())
    return text

def zipf_law(text):
    words = count_words_data(text)
    y_data = [v for k, v in sorted(words.items(), key=lambda x: x[1], reverse=True)]
    x_data = range(len(y_data))
    plt.plot(x_data, y_data)
    plt.xlim([0, 1000])
    plt.ylim([0, 1000])
    plt.show()

def hips_law(text):
    # Word count by text length
    data = {}
    for i in range(1, len(text), 1000):
        words = count_words_data(text[:i])
        data[i] = words
    x_plot_data = sorted(data.keys())
    y_plot_data = [len(v) for k, v in sorted(data.items(), key=lambda x: x[0])]
    plt.plot(x_plot_data, y_plot_data)
    plt.show()


text = normailized_text()
print('Total {} words'.format(len(text)))

hips_law(text)
zipf_law(text)
