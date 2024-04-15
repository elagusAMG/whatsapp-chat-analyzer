import pandas as pd
import plotly.express as px

def messages_per_month_over_years(df):
    date_df = df.groupby("date").size().reset_index(name="total_messages")
    # Converting 'date' column to datetime format
    date_df["date"] = pd.to_datetime(date_df["date"], format="%d/%m/%Y")

    # Formatting 'date' to display as month/year
    date_df["date"] = date_df["date"].dt.strftime("%b %Y")

    date_df["year"] = date_df["date"].str[-4:].astype(int)
    date_df["month"] = pd.to_datetime(date_df["date"], format="%b %Y").dt.month
    date_df = date_df.sort_values(by=["year", "month"])

    # Drop the temporary 'year' and 'month' columns
    date_df = date_df.drop(columns=["year", "month"])

    fig = px.bar(
        date_df, x="date", y="total_messages", title="Total Messages per Month"
    )
    fig.show()
