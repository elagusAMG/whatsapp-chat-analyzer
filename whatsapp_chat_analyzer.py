import seaborn as sns

sns.set_theme(style="white")

import warnings

warnings.simplefilter(action="ignore", category=UserWarning)

from utils.simple_stats import simple_stats
from utils.create_dataframe import create_dataframe
from utils.word_cloud import world_cloud
from utils.messages_per_month_over_years import messages_per_month_over_years


def main():
    """
    Main function for analyzing a WhatsApp group chat.

    How to run:
        $ python3 whatsapp_chat_analyzer.py
    """
    df = create_dataframe()
    stats = simple_stats(df)
    # print(stats)
    # world_cloud(df)
    # print(df)
    # most active
    #
    # Extract the hour from the time column
    df["hour"] = df["time"].str.split(":", expand=True)[0]
    # Plot the most active hours
    # plt.figure(figsize=[10, 8])
    # sns.barplot(x='count', y='hours', data=df['hour'].value_counts().rename_axis('hours').to_frame('count'), color='#F0D653')
    # plt.title('Most Active hours')
    # plt.xlabel('Number of Messages')
    # plt.ylabel('Hour')
    # plt.show()
    messages_per_month_over_years(df)


if __name__ == "__main__":
    main()
