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
    # print(simple_stats(df))

    # world_cloud(df)

    # most_active_hours(df)

    # messages_per_month_over_years(df)


if __name__ == "__main__":
    main()
