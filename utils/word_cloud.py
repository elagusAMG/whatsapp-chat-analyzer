import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def filter_words(message):
    words = message.split()
    filtered_words = [word for word in words if len(word) >= 4]
    return " ".join(filtered_words)


def world_cloud(dataframe):
    # Remove messages containing "Media omitted"
    x = dataframe[~dataframe["message"].str.contains("Media omitted")]

    # Concatenate all cleaned messages into a single string
    all_messages = x["message"].dropna().apply(filter_words).str.cat(sep=" ")

    # Generate word cloud
    wordcloud = WordCloud(
        width=800,
        height=800,
        background_color="white",
        stopwords=STOPWORDS,
        min_font_size=10,
    ).generate("".join(all_messages))

    # Plot word cloud
    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
