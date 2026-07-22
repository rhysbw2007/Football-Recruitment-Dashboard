import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

stats = pd.read_csv(
    BASE_DIR / "Data" / "Data1" / "players_data_light-2025_2026.csv"
)
light_stats_file_path="/Users/rhysbarker-white/Documents/Python work/FootballRecruitmentDashboard/Data/Data1/players_data_light-2025_2026.csv"
stats = pd.read_csv(light_stats_file_path, index_col="Player")
stats = stats.iloc[:,1:]
stats = stats.fillna(0)
stats.rename(columns={'Gls': 'Goals', 'Ast': 'Assists', 'TklW': 'Tackles Won', 'Fld': 'Fouled', 'Fls': 'Fouls','Crs': 'Crosses','Int': 'Interceptions'}, inplace=True)
stats.drop(columns=['GA','GA90','SoTA','Saves','Save%','W','D','L','CS','CS%','PKatt_stats_keeper','PKA','PKsv'], inplace=True)

fw_stats = stats[stats.Pos=='FW']
fw_stats_features = ['Age', 'Min' , 'Goals', 'Assists', 'PK','SoT/90','SoT%', 'G/Sh']
fw_stats = fw_stats[fw_stats_features]

top_scorers = stats.groupby(['Min','Sh','Comp','Pos']).Goals.max().sort_values(ascending=False).head(50)

stats["Gls_per90"] = stats["Goals"] / stats["Min"] * 90
stats["Ast_per90"] = stats["Assists"] / stats["Min"] * 90
stats["SoT/Sh"] = stats["SoT"]/stats["Sh"]

att_stats_features = ['Comp','Age','Min','Goals','Assists','Gls_per90','Ast_per90','Sh']
att_stats = stats[att_stats_features]

top_scorers = att_stats.sort_values('Gls_per90', ascending = False)
top_scorers = top_scorers[top_scorers.Min>450]
top20_scorers = top_scorers.head(20)

stats["G/Sh/90"]=stats["G/Sh"]/stats['Min']*90
top_finishers = stats.sort_values('G/Sh/90', ascending=False)
top10_finishers = top_finishers[top_finishers.Sh>50].head(10)

top_assisters = att_stats.sort_values('Ast_per90', ascending = False)
top20_assisters = top_assisters[top_assisters.Min>450].head(20)

player_profiles = pd.read_csv("/Users/rhysbarker-white/Documents/Python work/FootballRecruitmentDashboard/Data/Data2/all_player_profiles.csv")
player_profiles = player_profiles.merge(stats[['Squad']], left_on='name', right_index=True, how='left', suffixes=('', '_y'))
player_profiles.rename(columns={'Squad': 'squad'}, inplace=True)
player_profiles = player_profiles[['player_id', 'name', 'league', 'squad', 'position','market_value']]
player_stats = pd.read_csv("/Users/rhysbarker-white/Documents/Python work/FootballRecruitmentDashboard/Data/Data2/all_player_stats.csv")
merged_data = pd.merge(player_profiles, player_stats, on='player_id', how='inner')
merged_data.drop(columns=['player_id', 'league_y'], inplace=True)
merged_data.rename(columns={'name': 'Player', 'league_x': 'league'}, inplace=True)
merged_data.set_index('Player', inplace=True)
merged_data.fillna(0, inplace=True)

most_valuable_players = merged_data.sort_values('market_value', ascending=False).head(20)

stats = stats.merge(merged_data[['market_value','expected_goals','expected_assists','rating']], left_index=True, right_index=True, how='left')
stats_features = ['Nation','Comp','Squad','Pos','Age','market_value','MP','Starts','Min','Goals','expected_goals','Assists','expected_assists','G-PK','Gls_per90','Ast_per90','Sh','SoT','SoT%','Crosses','Tackles Won','Interceptions','Fouled','Fouls']
stats = stats[stats_features]

expected_goalsper90 = stats['expected_goals'] / stats['Min'] * 90
expected_assistsper90 = stats['expected_assists'] / stats['Min'] * 90

stats['expected_goalsper90'] = expected_goalsper90
stats['expected_assistsper90'] = expected_assistsper90

stats.drop_duplicates(inplace=True)

goal_overperformers = stats[(stats['Gls_per90'] > stats['expected_goalsper90']) & (stats['Min'] > 450)]
assist_overperformers = stats[(stats['Ast_per90'] > stats['expected_assistsper90']) & (stats['Min'] > 450)]
top_goal_overperformers = goal_overperformers.sort_values(['Gls_per90','Ast_per90'], ascending=False).head(20)
expectedGA_per90 = stats['expected_goalsper90'] + stats['expected_assistsper90']
stats['expected_GAper90'] = expectedGA_per90
creators = stats[stats['Min'] > 450].sort_values(['expected_GAper90'], ascending=False)