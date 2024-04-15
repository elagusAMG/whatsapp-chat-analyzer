import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def world_cloud(dataframe):
    # Remove messages containing "Media omitted"
    x = dataframe[~dataframe["message"].str.contains("Media omitted")]

    # Concatenate all cleaned messages into a single string
    all_messages = x["message"].dropna().str.cat(sep=" ")

    # Generate word cloud
    wordcloud = WordCloud(
        width=800,
        height=800,
        background_color="white",
        stopwords=STOPWORDS,
        min_font_size=10,
    ).generate(all_messages)

    # Plot word cloud
    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
