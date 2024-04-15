import seaborn as sns
import matplotlib.pyplot as plt

def most_active_hours(dataframe):
    plt.figure(figsize=[10, 8])
    sns.barplot(
        x="count",
        y="hours",
        data=dataframe["hour"].value_counts().rename_axis("hours").to_frame("count"),
        color="#F0D653",
    )
    plt.title("Most Active hours")
    plt.xlabel("Number of Messages")
    plt.ylabel("Hour")
    plt.show()
