import pandas as pd
import re

def simple_stats(dataframe):
    # Calculate messages sent per member
    messages_sent = dataframe.groupby("member")["message"].count()

    # Calculate words per message
    dataframe["words_per_message"] = dataframe["message"].apply(
        lambda x: len(x.split()) if isinstance(x, str) else 0
    )
    words_per_message = dataframe.groupby("member")["words_per_message"].mean()

    # Calculate emojis sent per message
    dataframe["emojis_per_message"] = dataframe["emojis"].apply(
        lambda x: len(x) if isinstance(x, list) else 0
    )
    emojis_per_message = dataframe.groupby("member")["emojis_per_message"].mean()

    # Calculate links sent per message
    dataframe["links_per_message"] = dataframe["message"].apply(
        lambda x: len(re.findall(r"http\S+", x)) if isinstance(x, str) else 0
    )
    links_per_message = dataframe.groupby("member")["links_per_message"].mean()

    # Combine stats into a single dataframe
    stats_dataframe = pd.concat(
        [messages_sent, words_per_message, emojis_per_message, links_per_message],
        axis=1,
    )
    stats_dataframe.columns = [
        "messages_sent",
        "words_per_message",
        "emojis_per_message",
        "links_per_message",
    ]

    # Sort by messages sent in descending order
    stats_dataframe = stats_dataframe.sort_values("messages_sent", ascending=False)

    # Print results
    return stats_dataframe
