import pandas as pd

#=============================
#  READ DATASET
#=============================

df1=pd.read_csv("IPL_Data_Analyzer/data.csv")
df2=pd.read_csv("IPL_Data_Analyzer/deliveries.csv")

print("="*50)
print("\n              IPL DATA ANALYZER ")
print("="*50)

#=============================
# MATCHES DATASET OVERVIEW
#=============================
print("\n1. Matches Data Overview")
print("-"*50)

print("\nTotal Matches : ",len(df1))
print("Total Seasons   :",df1["season"].nunique())
team1 = set(df1["team1"].dropna())
team2 = set(df1["team2"].dropna())

total_teams = len(team1.union(team2))
print("Total Teams   :",total_teams)
print("Total Venues  :",df1["venue"].nunique())
print("Total Cities  :",df1["city"].nunique())
print("Missing Values:",df1.isnull().sum().sum())
print("Duplicates    :",df1.duplicated().sum())
print("First season  :",df1["season"].min())
print("Latest season  :",df1["season"].max())

#=============================
# DELIVERIES DATASET OVERVIEW
#=============================
print("\nDELIVERIES DATASET OVERVIEW")
print("-" * 50)

print(f"Total Deliveries      : {len(df2)}")
Batsman1 = set(df2["batsman"].dropna())
Batsman2 = set(df2["non_striker"].dropna())
bowler = set(df2["bowler"].dropna())

all_batters = Batsman1.union(Batsman2)

total_batsman = len(all_batters)

total_player = len(
    all_batters.union(bowler)
)
print(f"Total Batters         : {total_batsman}")
print(f"Total Bowlers         : {df2['bowler'].nunique()}")
print(f"Total Batting Teams   : {df2['batting_team'].nunique()}")
print(f"Total Bowling Teams   : {df2['bowling_team'].nunique()}")
print(f"Missing Values        : {df2.isnull().sum().sum()}")
print(f"Duplicate Records     : {df2.duplicated().sum()}")
print(f"Total Runs Scored     : {df2['total_runs'].sum()}")
print(f"Total Wickets Fallen  : {df2['player_dismissed'].count()}")

#=================================
# TEAM ANALYSIS
#=================================

most_win = df1["winner"].value_counts()

print("\nTEAM ANALYSIS")
print("-" * 50)

print(f"Most Successful Team : {most_win.index[0]}")
print(f"Total Wins           : {most_win.iloc[0]}")

print("\nTOP 10 TEAMS BY WINS")
print("-" * 50)
team_analysis = pd.DataFrame({
    "Wins": most_win
})

print(team_analysis.head(10).to_string())

#========================================
# PLAYER OF THE MATCH ANALYSIS
#========================================

most_awards=df1["player_of_match"].value_counts()
print("\nPLAYER OF THE MATCH ANALYSIS")
print("-" * 50)

print(f"Most awardee Player : {most_awards.index[0]}")
print(f"Total Awards        : {most_awards.iloc[0]}")
print("\nTOP 10 PLAYERS BY AWARDS")
print("-" * 50)
award_analysis = pd.DataFrame({
    "Awards": most_awards
})
print(award_analysis.head(10).to_string())

#=======================================
# BATTING ANALYSIS
#=======================================
print("\nBATTING ANALYSIS")
print("-"*50)
most_runs=(
    df2.groupby("batsman")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
)
print(f"Highest Run Scorer = {most_runs.index[0]}")
print(f"Total runs         = {most_runs.iloc[0]}")
print("-"*50)
print("TOP 10 RUN SCORERS ")
print("-"*50)
runs_analysis=pd.DataFrame({
    "Runs":most_runs
})
print(runs_analysis.head(10).to_string())

#====================================
# FPURS ANALYSIS
#====================================
print("\n BOUNDARIES ANALYSIS ")
print("-"*50)
fours=df2[df2["batsman_runs"]==4]
most_fours=fours["batsman"].value_counts()
print(f"MOST FOURS PLAYER : {most_fours.index[0]}")
print(f"NUMBER OF FOURS    : {most_fours.iloc[0]}")

print("\nTOP 10 FOUR SCORERS ")
print("-"*50)
fours_analysis=pd.DataFrame({
    "Fours":most_fours
})
print(fours_analysis.head(10).to_string())

#====================================
# SIXES ANALYSIS
#====================================
print("\n SIXES ANALYSIS ")
print("-"*50)
sixes=df2[df2["batsman_runs"]==6]
most_sixes=sixes["batsman"].value_counts()
print(f"MOST SIXES PLAYER : {most_sixes.index[0]}")
print(f"NUMBER OF SIXES    : {most_sixes.iloc[0]}")

print("\nTOP 10 SIXES SCORERS ")
print("-"*50)
sixes_analysis=pd.DataFrame({
    "Sixes":most_sixes
})
print(sixes_analysis.head(10).to_string())


#==========================================
# BOWLING ANALYSIS 
#==========================================
print("\nBOWLING ANALYSIS ")
print("-"*50)
wickets=df2[df2["player_dismissed"].notna()]
most_wickets=wickets["bowler"].value_counts()
print(f"MOST WICKET TAKEN BY : {most_wickets.index[0]}")
print(f"NUMBER OF WICKETS    : {most_wickets.iloc[0]}")

print("\nTOP 10 WICKET TAKERS")
print("-"*50)
wickets_analysis=pd.DataFrame({
    "Wickets":most_wickets
})
print(wickets_analysis.head(10).to_string())

#=====================================
# DISMISSAL ANALYSIS
#=====================================
print("\nDISMISSAL ANALYSIS")
print("-"*50)
dismissal = df2["dismissal_kind"].value_counts()

dismissal_analysis = pd.DataFrame({
    "Count": dismissal
})

print(dismissal_analysis.to_string())
print(f"Most common Dismissal : {dismissal.index[0]}")
print(f"Total times occured   : {dismissal.iloc[0]}")


#======================================
# VENUE ANALYSIS
#======================================
print("\nVENUE ANALYSIS")
print('-'*50)

venue=df1["venue"].value_counts()

print(f"Most used venue : {venue.index[0]}")
print(f"Matches Played  : {venue.iloc[0]}")

venue_analysis=pd.DataFrame({
    "Matches Played":venue
})
print(venue_analysis.to_string())


#===================================
# SEASON ANALYSIS
#===================================
print("\nSEASON WISE ANALYSIS ")
print("-"*50)

season=df1["season"].value_counts()

print(f"Most active season : {season.index[0]}")
print(f"Matches Played     : {season.iloc[0]}")

season_analysis=pd.DataFrame({
    "Matches played":season
})

print(season_analysis.to_string())

#========================================
# OVERALL STATISTICS 
#========================================

print("\nOVERALL STATISTICS")
print("-"*50)

print(f"Total Matches : {len(df1)}")
print(f"Total seasons : {df1['season'].nunique()}")
print(f"Total teams   : {total_teams}")
print(f"Total Players : {total_player}")
print(f"Total venues  : {df1['venue'].nunique()}")
print(f"Total Runs    : {df2["total_runs"].sum()}")
print(f"Total Fours   : {most_fours.sum()}")
print(f"Total sixes   : {most_sixes.sum()}")
print(f"Total wickets : {most_wickets.sum()}")

df2.to_csv("IPL_Data_Analyzer/ipl_report.csv", index=False)
print("CSV Report Prepared Successfully")