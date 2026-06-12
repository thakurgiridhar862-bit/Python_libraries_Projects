import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# =========================================
# ZOMATO DATASET ANALYZER
# =========================================

df = pd.read_csv("Zomato_Data_Analyzer/zomato_clean.csv")

print("=" * 50)
print("                     ZOMATO DATA ANALYZER")
print("=" * 50)

# ===========================================
# DATASET OVERVIEW
# ===========================================

print("\nDATASET REVIEW")
print("-" * 50)

print(f"Total resturants      : {df['name'].nunique()}")
print(f"Total columns         : {len(df.columns)}")
print(f"Total locations       : {df['location'].nunique()}")
print(f"Total resturant types : {df['rest_type'].nunique()}")
print(f"Total cuisines        : {df['cuisines'].nunique()}")
print(f"Total missing values  : {df.isnull().sum().sum()}")
print(f"Total duplicates      : {df.duplicated().sum()}")


# ============================================
# RATING DATA CLEANING
# ============================================

rating_df = df.copy()

rating_df["rate"] = rating_df["rate"].replace("NEW", np.nan)
rating_df["rate"] = rating_df["rate"].replace("-", np.nan)
rating_df["rate"] = rating_df["rate"].str.replace("/5", "")
rating_df = rating_df.dropna(subset=["rate"])
rating_df["rate"] = rating_df["rate"].astype(float)

# =============================================
# RATING ANALYSIS
# =============================================

print("\n RATING ANALYSIS")
print("-" * 50)
print(f"Average Rating : {rating_df['rate'].mean().round(2)}")
print(f"Highest Rating : {rating_df['rate'].max()}")
print(f"Lowest Rating  : {rating_df['rate'].min()}")

print("\nTOP 10 HIGHLY POPULAR RESTURANTS ")
print("-" * 50)

high_rate = rating_df.groupby("name")["rate"].mean().round(2)
high_votes = rating_df.groupby("name")["votes"].mean().round(2)
popularity_analysis = pd.DataFrame(
    {"Average Rating": high_rate, "Average Votes": high_votes}
)

popularity_analysis["Popularity Score"] = (
    popularity_analysis["Average Rating"] * popularity_analysis["Average Votes"]
)

top_10 = popularity_analysis.sort_values(by="Popularity Score", ascending=False)

print("\nTOP 10 POPULAR RESTAURANTS")
print("-" * 50)
print(top_10.head(10).to_string())

# =================================
# LOCATION WISE ANALYSIS
# =================================
print("\n LOCATION WISE ANALYSIS")
print("-" * 50)
most_rest = df.groupby("location")["name"].nunique().sort_values(ascending=False)
print(f"Most resturant in : {most_rest.index[0]}")
print(f"NO of resturants  : {most_rest.iloc[0]}")

print("\nTOP 10 LOACTION WISE RESTURANTS")
print("-" * 50)

print(most_rest.head(10).to_string())

# ==============================================
# RESTURANT TYPE ANALYSIS
# ==============================================
print("\n RESTURANT TYPE ANALYSIS ")
print("-" * 50)
common_type = df.groupby("rest_type")["name"].nunique().sort_values(ascending=False)
print(f"Most common type resturant : {common_type.index[0]}")
print(f"Number of resturants of that type : {common_type.iloc[0]}")

print("\nTOP 10 RESTURANT TYPES")
print("-" * 50)
print(common_type.head(10).to_string())

# =======================================
# CUISINES ANALYSIS
# =======================================

cuisine_df = df.dropna(subset=["cuisines"]).copy()

cuisine_df["cuisines"] = cuisine_df["cuisines"].str.split(",")
cuisine_df = cuisine_df.explode("cuisines")
cuisine_df["cuisines"] = cuisine_df["cuisines"].str.strip()

print("\nCUISINES ANALYSIS")
print("-" * 50)
cuis = cuisine_df.groupby("cuisines")["name"].nunique().sort_values(ascending=False)
print(f"Most common cuisines : {cuis.index[0]}")
print(f"Number of resturants : {cuis.iloc[0]}")

print("\n TOP 10 RESTURANT ( CUISINES BASIS )")
print("-" * 50)
print(cuis.head(10).to_string())

# ===========================================
# COST ANALYSIS
# ===========================================

cost_df = df.dropna(subset=["approx_cost(for two people)"]).copy()
cost_df["approx_cost(for two people)"] = cost_df[
    "approx_cost(for two people)"
].str.replace(",", "")
cost_df["approx_cost(for two people)"] = cost_df[
    "approx_cost(for two people)"
].str.strip()
cost_df["approx_cost(for two people)"] = cost_df["approx_cost(for two people)"].astype(
    float
)

print("\n COST ANALYSIS")
print("-" * 50)
print(
    f"Average food cost    : {cost_df['approx_cost(for two people)'].mean().round(2)}"
)
print(f"Maximum cost for two : {cost_df['approx_cost(for two people)'].max()}")
print(f"Minimum cost for two : {cost_df['approx_cost(for two people)'].min()}")

price_variation = (
    cost_df.groupby("name")["approx_cost(for two people)"]
    .agg(
        Minimum_Cost="min",
        Maximum_Cost="max",
        Average_Cost="mean",
        Total_Records="count",
    )
    .round(2)
    .sort_values(by="Average_Cost", ascending=False)
)

print("\nTOP 10 MOST EXPENSIVE RESTAURANTS")
print("-" * 50)
print(price_variation.head(10).to_string())

# ===========================================
# ONLINE ORDER ANALYSIS
# ===========================================
print("=" * 50)
print("\n                ONLINE ORDER ANALYSIS")
print("=" * 50)

print("\nONLINE ORDER DISTIBUTION ")
print("-" * 50)

order = df.groupby("name")["online_order"].first().value_counts()
print(f"Resturants accepting online orders     : {order['Yes']}")
print(f"Resturants not accepting online orders : {order['No']}")

print("\nRATING COMPARISION")
print("-" * 50)
rate = rating_df.groupby("online_order")["rate"].mean().round(2)
print(f"Average rating (Online order = Yes) : {rate['Yes']}")
print(f"Average rating (Online order = No) : {rate['No']}")

print("\nVOTES COMPARISION")
print("-" * 50)
votes = df.groupby("online_order")["votes"].mean().round(2)

print(f"Average Votes (Online Order = Yes) : {votes['Yes']}")
print(f"Average Votes (Online Order = No)  : {votes['No']}")

print("\n IMPORTANT CONCLUSION")
print("-" * 50)
if order["Yes"] > order["No"]:
    print("1. Most restaurants provide online order.")
else:
    print("1. Most restaurants do not provide online order.")
if rate["Yes"] > rate["No"]:
    print("2. Online ordering restaurants have better ratings.")
else:
    print("2. Online ordering restaurants have worse ratings.")
if votes["Yes"] > votes["No"]:
    print("3. Online ordering restaurants receive higher engagement.")
else:
    print("3. Online ordering restaurants receive lower engagement.")


# ===========================================
# TABLE BOOKING ANALYSIS
# ===========================================
print("=" * 50)
print("\n                TABLE BOOKING ANALYSIS")
print("=" * 50)

print("\nTABLE BOOKING DISTIBUTION ")
print("-" * 50)

table = df.groupby("name")["book_table"].first().value_counts()
print(f"Resturants with table booking     : {table['Yes']}")
print(f"Resturants without table booking  : {table['No']}")

print("\nRATING COMPARISION")
print("-" * 50)
rate_table = rating_df.groupby("book_table")["rate"].mean().round(2)
print(f"Average rating (Table booking = Yes) : {rate_table['Yes']}")
print(f"Average rating (Table booking = No) : {rate_table['No']}")

print("\nVOTES COMPARISION")
print("-" * 50)
votes_table = df.groupby("book_table")["votes"].mean().round(2)

print(f"Average Votes (Table Booking = Yes) : {votes_table['Yes']}")
print(f"Average Votes (Table Booking = No)  : {votes_table['No']}")

print("\nCOST COMPARISION")
print("-" * 50)
cost_table = (
    cost_df.groupby("book_table")["approx_cost(for two people)"].mean().round(2)
)
print(f"Average cost (Table Booking = Yes) : {cost_table['Yes']}")
print(f"Average cost (Table Booking = No)  : {cost_table['No']}")

print("\n IMPORTANT CONCLUSION")
print("-" * 50)
if table["Yes"] > table["No"]:
    print("1. Most restaurants provide table booking.")
else:
    print("1. Most restaurants do not provide table booking.")
if rate_table["Yes"] > rate_table["No"]:
    print("2. Table Booking restaurants have better ratings.")
else:
    print("2. Table Booking restaurants have worse ratings.")
if votes_table["Yes"] > votes_table["No"]:
    print("3. Table Booking restaurants receive higher engagement.")
else:
    print("3. Table Booking restaurants receive lower engagement.")
if cost_table["Yes"] > cost_table["No"]:
    print("4. Table Booking restaurants are more expensive. ")
else:
    print("4. Table Booking restaurants are less expensive. ")

# ===========================================
# VOTES ANALYSIS
# ===========================================
print("=" * 50)
print("\nVOTES ANALYSIS")
print("=" * 50)

avg_votes = df["votes"].mean().round(2)
high_vote = df["votes"].max()
print(f"Average votes across dataset : {avg_votes}")
print(f"Highest votes across dataset : {high_vote}")

print("\nTOP 10 HIGHLY VOTED RESTURANTS")
print("-" * 50)
top_10votes = df.groupby("name")["votes"].mean().round(2).sort_values(ascending=False)
print(top_10votes.head(10).to_string())


# =======================================
# FINAL BUISNESS INSIGHTS
# =======================================
print("=" * 50)
print("\n                FINAL BUISNESS INSIGHTS ")
print("=" * 50)
print("1. white field has the highest number of restaurants.")
print("2. Quick bite is the most common restaurant type.")
print("3. North indian is the most popular cuisine.")
print(
    "4. Online ordering and table booking facilities are associated with stronger restaurant performance."
)
print("5. Customer engagement (votes) plays a major role in restaurant popularity.")
print("6. Restaurant prices vary significantly across locations and restaurant types.")
print(
    "7. A small number of restaurants attract exceptionally high customer attention compared to the rest of the market."
)
# ===========================================
# EXPORT FINAL SUMMARY TO CSV
# ===========================================

summary_data = {
    "Metric": [
        "Total Restaurants",
        "Total Columns",
        "Total Locations",
        "Total Restaurant Types",
        "Total Cuisines",
        "Total Missing Values",
        "Total Duplicates",
        "Average Rating",
        "Highest Rating",
        "Lowest Rating",
        "Most Popular Restaurant",
        "Most Restaurants Location",
        "Most Common Restaurant Type",
        "Most Common Cuisine",
        "Average Food Cost",
        "Maximum Cost For Two",
        "Minimum Cost For Two",
        "Restaurants Accepting Online Orders",
        "Restaurants Not Accepting Online Orders",
        "Restaurants With Table Booking",
        "Restaurants Without Table Booking",
        "Average Votes Across Dataset",
        "Highest Votes Across Dataset",
    ],
    "Value": [
        df["name"].nunique(),
        len(df.columns),
        df["location"].nunique(),
        df["rest_type"].nunique(),
        df["cuisines"].nunique(),
        df.isnull().sum().sum(),
        df.duplicated().sum(),
        rating_df["rate"].mean().round(2),
        rating_df["rate"].max(),
        rating_df["rate"].min(),
        top_10.index[0],
        most_rest.index[0],
        common_type.index[0],
        cuis.index[0],
        cost_df["approx_cost(for two people)"].mean().round(2),
        cost_df["approx_cost(for two people)"].max(),
        cost_df["approx_cost(for two people)"].min(),
        order["Yes"],
        order["No"],
        table["Yes"],
        table["No"],
        df["votes"].mean().round(2),
        df["votes"].max(),
    ],
}


# ===========================================
# VISUALISATION PROCESS
# ===========================================

# GRAPH 1 (TOP 10 RESTURANTS)
x1 = top_10.head(10).index
y1 = top_10.head(10)["Popularity Score"].values
fig, axes1 = plt.subplots(1, 1, figsize=(16, 5))
plt.subplots_adjust(left=0.17)

axes1.set_title("Top 10 Resturants")
axes1.set_xlabel("Popularity score")
axes1.set_ylabel("Resturant name")
color1 = ["green" if v == max(y1) else "red" if v == min(y1) else "blue" for v in y1]
bar1 = axes1.barh(x1, y1, color=color1)
axes1.bar_label(bar1, labels=[f"{v:.0f}" for v in y1], padding=5)
axes1.invert_yaxis()
axes1.grid(axis="x", linestyle="--", alpha=0.4)
plt.savefig(
    "Zomato_Data_Analyzer/graphs/top10_resturants.png", dpi=300, bbox_inches="tight"
)


# GRAPH 2 FOR TOP 10 LACATIONS
x2 = most_rest.head(10).index
y2 = most_rest.head(10).values
fig, axes2 = plt.subplots(1, 1, figsize=(16, 5))
axes2.set_title("Top 10 Loaction by number of resturants")
axes2.set_xlabel("Number of Resturants")
axes2.set_ylabel("Location ")
color2 = ["green" if v == max(y2) else "red" if v == min(y2) else "blue" for v in y2]
bar2 = axes2.barh(x2, y2, color=color2)
axes2.bar_label(bar2, labels=[f"{v:.0f}" for v in y2], padding=5)
axes2.invert_yaxis()
axes2.grid(axis="y", linestyle="--", alpha=0.3)
plt.savefig(
    "Zomato_Data_Analyzer/graphs/top10_locations.png", dpi=300, bbox_inches="tight"
)


# GRAPH 3 FOR TOP 10 RESTURANT TYPES
x3 = common_type.head(10).index
y3 = common_type.head(10).values
fig, axes3 = plt.subplots(1, 1, figsize=(16, 5))
axes3.set_title("Top 10 Resturants types")
axes3.set_xlabel("Resturant types")
axes3.set_ylabel("Number of resturants ")
color3 = ["green" if v == max(y3) else "red" if v == min(y3) else "blue" for v in y3]
bar3 = axes3.bar(x3, y3, color=color3)
axes3.bar_label(bar3, labels=[f"{v:.0f}" for v in y3], padding=5)
axes3.grid(axis="x", linestyle="--", alpha=0.3)
plt.xticks(rotation=45)
plt.savefig(
    "Zomato_Data_Analyzer/graphs/top10_Resturant_types.png",
    dpi=300,
    bbox_inches="tight",
)


# GRAPH 4 FOR TOP 10 CUISINES TYPES
x4 = cuis.head(10).index
y4 = cuis.head(10).values
fig, axes4 = plt.subplots(1, 1, figsize=(16, 5))
axes4.set_title("Top 10 Cuisines Types")
axes4.set_xlabel("Number Of Resturnats")
axes4.set_ylabel("Cuisine Type ")
color4 = ["green" if v == max(y4) else "red" if v == min(y4) else "blue" for v in y4]
bar4 = axes4.barh(x4, y4, color=color4)
axes4.invert_yaxis()
axes4.bar_label(bar4, labels=[f"{v:.0f}" for v in y4], padding=5)
axes4.grid(axis="y", linestyle="--", alpha=0.3)
plt.savefig(
    "Zomato_Data_Analyzer/graphs/top10_cuisines_types.png",
    dpi=300,
    bbox_inches="tight",
)

# GRAPH 5
fig, axes5 = plt.subplots(1, 1, figsize=(16, 5))
axes5.set_title("Resturant Rating Distibution")
axes5.set_xlabel("Rating")
axes5.set_ylabel("Number of Resturants")
axes5.hist(rating_df["rate"], bins=20, color="lightgreen")
axes5.grid(axis="y", linestyle="--", alpha=0.3)
avg_rating = rating_df["rate"].mean().round(2)
axes5.axvline(
    x=avg_rating,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average ({avg_rating:.2f})",
)
axes5.legend()
plt.savefig(
    "Zomato_Data_Analyzer/graphs/Rating_wise_Resturant_dist.png",
    dpi=300,
    bbox_inches="tight",
)


# GRAPH 6
fig, axes6 = plt.subplots(1, 1, figsize=(16, 5))
axes6.set_title("Cost Distribution for Two People")
axes6.set_xlabel("Approx Cost for Two People (₹)")
axes6.set_ylabel("Number of Resturants")
axes6.hist(cost_df["approx_cost(for two people)"], bins=20, color="lightblue")
axes6.grid(axis="y", linestyle="--", alpha=0.3)
avg_cost = cost_df["approx_cost(for two people)"].mean().round(2)
axes6.axvline(
    x=avg_cost,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average ({avg_cost:.2f})",
)
axes6.legend()
plt.savefig(
    "Zomato_Data_Analyzer/graphs/cost_wise_Resturant_dist.png",
    dpi=300,
    bbox_inches="tight",
)


# GRAPH 7 : ONLINE ORDER DISTRIBUTION

online_order_count = df["online_order"].value_counts()

fig, axes7 = plt.subplots(1, 1, figsize=(8, 6))

axes7.set_title("Online Order Availability Distribution")

axes7.pie(
    online_order_count.values,
    labels=online_order_count.index,
    autopct="%1.1f%%",
    startangle=90,
    shadow=False,
    explode=[0.05, 0],
    textprops={"fontsize": 15},
)

axes7.axis("equal")

plt.savefig(
    "Zomato_Data_Analyzer/graphs/online_order_distribution.png",
    dpi=300,
    bbox_inches="tight",
)


# GRAPH 8 : TABLE BOOKING DISTRIBUTION

book_table_count = df["book_table"].value_counts()

fig, axes8 = plt.subplots(1, 1, figsize=(8, 6))

axes8.set_title("Table Booking Availability Distribution")

axes8.pie(
    book_table_count.values,
    labels=book_table_count.index,
    autopct="%1.1f%%",
    startangle=90,
    shadow=False,
    explode=[0.05, 0],
    textprops={"fontsize": 15},
)

axes8.axis("equal")

plt.savefig(
    "Zomato_Data_Analyzer/graphs/table_booking_distribution.png",
    dpi=300,
    bbox_inches="tight",
)


summary_df = pd.DataFrame(summary_data)

summary_df.to_csv("Zomato_Data_Analyzer/zomato_summary.csv", index=False)

print("\nFINAL SUMMARY CSV CREATED SUCCESSFULLY!")
print("-" * 50)
print("File saved as : Zomato_Data_Analyzer/zomato_summary.csv")
