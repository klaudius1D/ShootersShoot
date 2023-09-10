import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv("topPicksCSV/Playoffs-Master-CombinedLR_topPicks.csv")
# sort by suggested_fantasypoints_rank
df = df.sort_values(by=["Suggested_FantasyPoints_Rank"], ascending=True)

# find player
player_search = df[df["Player"].str.contains("Shai Gilgeous-Alexander", case=False)]

# find top 10 players  on all columns
columns_to_show = ["PTS", "TRB", "AST", "STL", "TOV", "BLK", "FantasyPoints", "MP"]
for column in columns_to_show:
    print(df.sort_values(by=[column], ascending=False).head(10)[["Player", column]])

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
