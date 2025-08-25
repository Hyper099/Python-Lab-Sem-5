from wordcloud import WordCloud
import matplotlib.pyplot as plt

t = "helllo world i am jayneel"

wc = WordCloud(width=100, height=100).generate(t);

plt.imshow(wc)
