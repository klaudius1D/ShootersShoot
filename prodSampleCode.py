import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("topPicksCSV/Playoffs-Master-CombinedLR_topPicks.csv")
# sort by suggested_fantasypoints_rank
df = df.sort_values(by=["Suggested_FantasyPoints_Rank"], ascending=True)

# find player
player_search = df[df["Player"].str.contains("lebron", case=False)]

# find top 10 players  on all columns
top_10_players = df.head(10)
top_10_scorers = df.sort_values(by=["PTS"], ascending=False).head(10)
top_10_rebounders = df.sort_values(by=["TRB"], ascending=False).head(10)
top_10_most_assists = df.sort_values(by=["AST"], ascending=False).head(10)
top_10_most_steals = df.sort_values(by=["STL"], ascending=False).head(10)
top_10_most_tov = df.sort_values(by=["TOV"], ascending=False).head(10)
top_10_most_blocks = df.sort_values(by=["BLK"], ascending=False).head(10)
top_10_highest_fp = df.sort_values(by=["FantasyPoints"], ascending=False).head(10)
top_10_most_mp = df.sort_values(by=["MP"], ascending=False).head(10)

# using seaborn to plot bar graph for top 10 players with highest suggested fantasy points
sns.set(style="whitegrid")
ax = sns.barplot(x="Suggested_FantasyPoints", y="Player", data=top_10_players)
plt.title("Top 10 Players with Highest Fantasy Points in Playoffs")
plt.xlabel("Points")
plt.ylabel("Player")


# include suggested fantasy points in each bar
for p in ax.patches:
    width = p.get_width()
    plt.text(
        0.5 + p.get_width(),
        p.get_y() + 0.55 * p.get_height(),
        "{:1.0f}".format(width),
        ha="center",
        va="center",
    )
plt.show()
