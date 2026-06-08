import pandas as pd
import numpy as np

#=========================================
# ZOMATO DATASET ANALYZER
#=========================================

df=pd.read_csv("Zomato_Data_Analyzer/zomato_clean.csv")

print("="*50)
print("                     ZOMATO DATA ANALYZER")
print("="*50)

#===========================================
# DATASET OVERVIEW
#===========================================

print("\nDATASET REVIEW")
print("-"*50)

print(f"Total resturants      : {df["name"].nunique()}")
print(f"Total columns         : {len(df.columns)}")
print(f"Total locations       : {df['location'].nunique()}")
print(f"Total resturant types : {df['rest_type'].nunique()}")
print(f"Total cuisines        : {df['cuisines'].nunique()}")
print(f"Total missing values  : {df.isnull().sum().sum()}")
print(f"Total duplicates      : {df.duplicated().sum()}")


#============================================
# RATING DATA CLEANING 
#============================================

rating_df = df.copy()

rating_df['rate'] = rating_df['rate'].replace('NEW', np.nan)
rating_df['rate'] = rating_df['rate'].replace('-', np.nan)
rating_df['rate'] = rating_df['rate'].str.replace('/5', '')
rating_df = rating_df.dropna(subset=['rate'])
rating_df['rate'] = rating_df['rate'].astype(float)

#=============================================
# RATING ANALYSIS
#=============================================

print("\n RATING ANALYSIS")
print("-"*50)
print(f"Average Rating : {rating_df['rate'].mean().round(2)}")
print(f"Highest Rating : {rating_df['rate'].max()}")
print(f"Lowest Rating  : {rating_df['rate'].min()}")

print("\nTOP 10 HIGHLY POPULAR RESTURANTS ")
print("-"*50)

high_rate=(
    rating_df.groupby("name")["rate"]
    .mean()
    .round(2)
)
high_votes=(
    rating_df.groupby("name")["votes"]
    .mean()
    .round(2)
)
popularity_analysis = pd.DataFrame({
    "Average Rating": high_rate,
    "Average Votes": high_votes
})

popularity_analysis["Popularity Score"] = (
    popularity_analysis["Average Rating"] *
    popularity_analysis["Average Votes"]
)

top_10 = popularity_analysis.sort_values(
    by="Popularity Score",
    ascending=False
)

print("\nTOP 10 POPULAR RESTAURANTS")
print("-" * 50)
print(top_10.head(10).to_string())

#=================================
# LOCATION WISE ANALYSIS
#=================================
print("\n LOCATION WISE ANALYSIS")
print("-"*50)
most_rest=(
    df.groupby('location')["name"]
    .nunique().
    sort_values(ascending=False)
)
print(f"Most resturant in : {most_rest.index[0]}")
print(f"NO of resturants  : {most_rest.iloc[0]}")

print("\nTOP 10 LOACTION WISE RESTURANTS")
print("-"*50)

print(most_rest.head(10).to_string())

#==============================================
# RESTURANT TYPE ANALYSIS
#==============================================
print("\n RESTURANT TYPE ANALYSIS ")
print("-"*50)
common_type=(
    df.groupby('rest_type')["name"]
    .nunique()
    .sort_values(ascending=False)
)
print(f"Most common type resturant : {common_type.index[0]}")
print(f"Number of resturants of that type : {common_type.iloc[0]}")

print("\nTOP 10 RESTURANT TYPES")
print("-"*50)
print(common_type.head(10).to_string())

#=======================================
# CUISINES ANALYSIS
#=======================================

cuisine_df = df.dropna(subset=["cuisines"]).copy()

cuisine_df["cuisines"] = cuisine_df["cuisines"].str.split(",")
cuisine_df = cuisine_df.explode("cuisines")
cuisine_df["cuisines"] = cuisine_df["cuisines"].str.strip()

print("\nCUISINES ANALYSIS")
print("-"*50)
cuis=(
    cuisine_df.groupby("cuisines")["name"]
    .nunique()
    .sort_values(ascending=False)
)
print(f"Most common cuisines : {cuis.index[0]}")
print(f"Number of resturants : {cuis.iloc[0]}")

print("\n TOP 10 RESTURANT ( CUISINES BASIS )")
print("-"*50)
print(cuis.head(10).to_string())

#===========================================
# COST ANALYSIS
#===========================================

cost_df=df.dropna(subset=["approx_cost(for two people)"]).copy()
cost_df["approx_cost(for two people)"]=cost_df["approx_cost(for two people)"].str.replace(",","")
cost_df["approx_cost(for two people)"]=cost_df["approx_cost(for two people)"].str.strip()
cost_df["approx_cost(for two people)"]=cost_df["approx_cost(for two people)"].astype(float)

print("\n COST ANALYSIS")
print("-"*50)
print(f"Average food cost    : {cost_df['approx_cost(for two people)'].mean().round(2)}")
print(f"Maximum cost for two : {cost_df['approx_cost(for two people)'].max()}")
print(f"Minimum cost for two : {cost_df['approx_cost(for two people)'].min()}")

price_variation = (
    cost_df.groupby("name")["approx_cost(for two people)"]
    .agg(
        Minimum_Cost="min",
        Maximum_Cost="max",
        Average_Cost="mean",
        Total_Records="count"
    )
    .round(2)
    .sort_values(by="Average_Cost", ascending=False)
)

print("\nTOP 10 MOST EXPENSIVE RESTAURANTS")
print("-"*50)
print(price_variation.head(10).to_string())

#===========================================
# ONLINE ORDER ANALYSIS
#===========================================
print("="*50)
print("\n                ONLINE ORDER ANALYSIS")
print("="*50)

print("\nONLINE ORDER DISTIBUTION ")
print("-"*50)

order=(
    df.groupby("name")["online_order"]
    .first()
    .value_counts()
)
print(f"Resturants accepting online orders     : {order['Yes']}")
print(f"Resturants not accepting online orders : {order['No']}")

print("\nRATING COMPARISION")
print("-"*50)
rate=(
    rating_df.groupby("online_order")["rate"]
    .mean()
    .round(2)
)
print(f"Average rating (Online order = Yes) : {rate["Yes"]}")
print(f"Average rating (Online order = No) : {rate["No"]}")

print("\nVOTES COMPARISION")
print("-"*50)
votes = (
    df.groupby("online_order")["votes"]
    .mean()
    .round(2)
)

print(f"Average Votes (Online Order = Yes) : {votes['Yes']}")
print(f"Average Votes (Online Order = No)  : {votes['No']}")

print("\n IMPORTANT CONCLUSION")
print("-"*50)
if(order["Yes"]>order["No"]):
    print("1. Most restaurants provide online order.")
else :
    print("1. Most restaurants do not provide online order.")
if(rate["Yes"]>rate["No"]):
    print("2. Online ordering restaurants have better ratings.")
else :
    print("2. Online ordering restaurants have worse ratings.")
if(votes["Yes"]>votes["No"]):
    print("3. Online ordering restaurants receive higher engagement.")
else:
    print("3. Online ordering restaurants receive lower engagement.")
    

#===========================================
# TABLE BOOKING ANALYSIS
#===========================================
print("="*50)
print("\n                TABLE BOOKING ANALYSIS")
print("="*50)

print("\nTABLE BOOKING DISTIBUTION ")
print("-"*50)

table=(
    df.groupby("name")["book_table"]
    .first()
    .value_counts()
)
print(f"Resturants with table booking     : {table['Yes']}")
print(f"Resturants without table booking  : {table['No']}")

print("\nRATING COMPARISION")
print("-"*50)
rate_table=(
    rating_df.groupby("book_table")["rate"]
    .mean()
    .round(2)
)
print(f"Average rating (Table booking = Yes) : {rate_table["Yes"]}")
print(f"Average rating (Table booking = No) : {rate_table["No"]}")

print("\nVOTES COMPARISION")
print("-"*50)
votes_table = (
    df.groupby("book_table")["votes"]
    .mean()
    .round(2)
)

print(f"Average Votes (Table Booking = Yes) : {votes_table['Yes']}")
print(f"Average Votes (Table Booking = No)  : {votes_table['No']}")

print("\nCOST COMPARISION")
print("-"*50)
cost_table=(
    cost_df.groupby("book_table")["approx_cost(for two people)"]
    .mean()
    .round(2)
)
print(f"Average cost (Table Booking = Yes) : {cost_table['Yes']}")
print(f"Average cost (Table Booking = No)  : {cost_table['No']}")

print("\n IMPORTANT CONCLUSION")
print("-"*50)
if(table["Yes"]>table["No"]):
    print("1. Most restaurants provide table booking.")
else :
    print("1. Most restaurants do not provide table booking.")
if(rate_table["Yes"]>rate_table["No"]):
    print("2. Table Booking restaurants have better ratings.")
else :
    print("2. Table Booking restaurants have worse ratings.")
if(votes_table["Yes"]>votes_table["No"]):
    print("3. Table Booking restaurants receive higher engagement.")
else:
    print("3. Table Booking restaurants receive lower engagement.")
if(cost_table["Yes"]>cost_table["No"]):
    print("4. Table Booking restaurants are more expensive. ")
else:
    print("4. Table Booking restaurants are less expensive. ")
    
#===========================================
# VOTES ANALYSIS
#===========================================
print("="*50)
print("\nVOTES ANALYSIS")
print("="*50)

avg_votes=df["votes"].mean().round(2)
high_vote=df["votes"].max()
print(f"Average votes across dataset : {avg_votes}")
print(f"Highest votes across dataset : {high_vote}")

print("\nTOP 10 HIGHLY VOTED RESTURANTS")
print("-"*50)
top_10votes=(
    df.groupby("name")["votes"]
    .mean()
    .round(2)
    .sort_values(ascending = False)
)
print(top_10votes.head(10).to_string())


#=======================================
# FINAL BUISNESS INSIGHTS 
#=======================================
print("="*50)
print("\n                FINAL BUISNESS INSIGHTS ")
print("="*50)
print("1. white field has the highest number of restaurants.")
print("2. Quick bite is the most common restaurant type.")
print("3. North indian is the most popular cuisine.")
print("4. Online ordering and table booking facilities are associated with stronger restaurant performance.")
print("5. Customer engagement (votes) plays a major role in restaurant popularity.")
print("6. Restaurant prices vary significantly across locations and restaurant types.")
print("7. A small number of restaurants attract exceptionally high customer attention compared to the rest of the market.")
#===========================================
# EXPORT FINAL SUMMARY TO CSV
#===========================================

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
        "Highest Votes Across Dataset"
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
        df["votes"].max()
    ]
}

summary_df = pd.DataFrame(summary_data)

summary_df.to_csv("Zomato_Data_Analyzer/zomato_summary.csv", index=False)

print("\nFINAL SUMMARY CSV CREATED SUCCESSFULLY!")
print("-"*50)
print("File saved as : Zomato_Data_Analyzer/zomato_summary.csv")