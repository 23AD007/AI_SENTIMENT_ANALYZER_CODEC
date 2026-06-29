from wordcloud import WordCloud
import matplotlib.pyplot as plt

def create_wordcloud(text):

    wc = WordCloud(
        width=1000,
        height=500,
        background_color="white"
    ).generate(text)

    plt.figure(figsize=(10,5))
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig("static/wordcloud.png")
    plt.close()