import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np
import plotly.express as px

from data import (stats, top10_finishers, top20_assisters, top20_scorers, merged_data, most_valuable_players, goal_overperformers, assist_overperformers, creators)
from plots import (plot_top_finishers, plot_top_assisters, plot_top_scorers)

st.title("Football Recruitment Dashboard")
add_sidebar = st.sidebar.selectbox('Select Category', options=['Home','Advanced Stats','Compare 2 Players','Recruitment'], key='category')

if add_sidebar == 'Home':
    st.write("Welcome to the Football Recruitment Dashboard!")
    selected_player = st.selectbox("Select a player to view their stats", options=stats.index, index=stats.index.get_loc('Phil Foden'), key='player')
    st.dataframe(stats.loc[selected_player])
    selected_league = st.selectbox("Select a league to view the top goal scorers", options=stats['Comp'].unique(), key='league')
    league_top_scorers = stats[stats['Comp'] == selected_league].sort_values('Goals', ascending=False).head(10)
    st.write(f"Top 10 goal scorers in {selected_league}:")
    st.dataframe(league_top_scorers[['Squad','Min','Goals']])
    selected_nation = st.selectbox("Select a nation to view the top goal scorers", options=stats['Nation'].unique(), key='nation')
    nation_top_scorers = stats[stats['Nation'] == selected_nation].sort_values('Goals', ascending=False).head(10)
    st.write(f"Top 10 goal scorers in {selected_nation}:")
    st.dataframe(nation_top_scorers[['Squad','Min','Goals']])


if add_sidebar == 'Advanced Stats':
    st.title("Advanced Statistics")
    st.write("This section contains advanced statistical analysis of player performance.")

    st.title("Top 20 Goal Scorers Per 90")
    st.write("This table shows the top 20 goal scorers based on goals per 90 minutes played.")
    st.dataframe(top20_scorers)
    st.write("This chart shows the top 20 goal scorers based on goals per 90 minutes played.")
    fig, ax = plt.subplots(figsize=(14,8))
    ax.bar(top20_scorers.index, top20_scorers['Gls_per90'])
    ax.set_xticklabels(top20_scorers.index, rotation=45, ha='right')
    ax.set_xlabel("Player", fontsize=12)
    ax.set_ylabel("Goals per 90", fontsize=12)
    ax.set_title("Top 20 Goal Scorers Per 90", fontsize=14)
    st.pyplot(fig)

    st.title("Top 20 Assisters Per 90")
    st.write("This table shows the top 20 assisters based on assists per 90 minutes played.")
    st.dataframe(top20_assisters)
    st.write("This chart shows the top 20 assisters based on assists per 90 minutes played.")
    fig, ax = plt.subplots(figsize=(14,8))
    ax.bar(top20_assisters.index, top20_assisters['Ast_per90'])
    ax.set_xticklabels(top20_assisters.index, rotation=45, ha='right')
    ax.set_xlabel("Player", fontsize=12)
    ax.set_ylabel("Assists per 90", fontsize=12)
    ax.set_title("Top 20 Assisters Per 90", fontsize=14)
    st.pyplot(fig)

    st.title("Top 10 Finishers")
    st.write("This table shows the top 10 finishers based on goals per 90 minutes played against shots per 90 minutes played.")
    st.dataframe(top10_finishers[['Comp','Age','Min','Sh/90', 'Gls_per90']])
    st.write("This chart shows the top 10 finishers based on goals per 90 minutes played against shots per 90 minutes played.")
    fig, ax = plt.subplots(figsize=(14,8))
    ax.scatter(top10_finishers['Sh/90'], top10_finishers['Gls_per90'])
    for i, player in enumerate(top10_finishers.index):
        ax.annotate(player, (top10_finishers['Sh/90'][i], top10_finishers['Gls_per90'][i]),size=10, ha='left', va='bottom')
    ax.set_xlabel("Shots per 90", fontsize=12)
    ax.set_ylabel("Goals per 90", fontsize=12)
    ax.set_title("Top 10 Finishers", fontsize=14)
    st.pyplot(fig)

    st.title("Most Valuable Players")
    st.write("This table shows the top 20 most valuable players based on market value.")
    st.dataframe(most_valuable_players[['league','squad','position','market_value']])
    fig, ax = plt.subplots(figsize=(14,8))
    ax.bar(most_valuable_players.index, most_valuable_players['market_value'])
    ax.set_xticklabels(most_valuable_players.index, rotation=45, ha='right')
    ax.set_xlabel("Player", fontsize=12)
    ax.set_ylabel("Market Value", fontsize=12)
    ax.set_title("Most Valuable Players", fontsize=14)
    st.pyplot(fig)

if add_sidebar == 'Compare 2 Players':
    st.title("Compare 2 Players")
    st.write("Select two players to compare their stats.")
    player1 = st.selectbox("Select Player 1", options=stats.index, index=stats.index.get_loc('Phil Foden'))
    player2 = st.selectbox("Select Player 2", options=stats.index, index=stats.index.get_loc('Kevin De Bruyne'))
    st.write(f"Comparing {player1} and {player2}")
    st.dataframe(stats.loc[[player1, player2]])
    xdata = stats.loc[[player1 , player2]]
    xdata1 = xdata[['Age','MP','Starts','Goals','Assists','G-PK', 'Tackles Won','Fouled','Fouls']]
    fig1, ax1 = plt.subplots(figsize=(14,8))
    x1=np.arange(len(xdata1.columns))
    width=0.35
    ax1.bar(x1-width/2, xdata1.loc[player1], width, label=player1)
    ax1.bar(x1+width/2, xdata1.loc[player2], width, label=player2)
    ax1.set_xticks(x1, labels=xdata1.columns)
    ax1.set_title(f"Comparison of {player1} and {player2}", fontsize=14)
    ax1.legend()
    st.pyplot(fig1)
    xdata2 = xdata[['Gls_per90','Ast_per90','expected_goalsper90','expected_assistsper90']]
    fig2, ax2 = plt.subplots(figsize=(14,8))
    x2=np.arange(len(xdata2.columns))
    width=0.35
    ax2.bar(x2-width/2, xdata2.loc[player1], width, label=player1)
    ax2.bar(x2+width/2, xdata2.loc[player2], width, label=player2)
    ax2.set_xticks(x2, labels=xdata2.columns)
    ax2.set_title(f"Comparison of {player1} and {player2} (Per 90 Stats)", fontsize=14)
    ax2.legend()
    st.pyplot(fig2)

top_goal_overperformers = goal_overperformers.sort_values(['Gls_per90','Ast_per90'], ascending=False).head(20)
top_assist_overperformers = assist_overperformers.sort_values(['Ast_per90','Gls_per90'], ascending=False).head(20)
top_creators = creators.head(20)

if add_sidebar == 'Recruitment':
    st.title("Recruitment")
    st.write("This section contains information on potential recruitment targets based on player performance.")
    st.write("My recruitment targets based on your budget and position requirements")
    arg1 = st.selectbox("Select your budget (in millions):", options=range(0, 251, 10), index=5, key='budget')
    arg2 = st.selectbox("Select the position you are looking for:", options=['FW','MF','DF'], key='position') 
    filtered_creators = (creators[(creators['market_value'] <= arg1*1e6) & (creators['Pos'] == arg2)].sort_values(['Gls_per90','Ast_per90'], ascending=False).head(10)[['Comp','Squad','Pos','Age','market_value','Min','Gls_per90','expected_goalsper90','Ast_per90','expected_assistsper90']])
    st.dataframe(filtered_creators)

    fig = px.scatter(
        filtered_creators,
        x="expected_assistsper90",
        y="expected_goalsper90",
        color="market_value",          # Colour represents market value
        size="market_value",           # Bubble size also represents market value
        hover_name=filtered_creators.index,
        hover_data={
            "Comp": True,
            "Squad": True,
            "Age": True,
            "market_value": ":,.0f",
            "Gls_per90": ":.2f",
            "Ast_per90": ":.2f",
            "expected_goalsper90": ":.2f",
            "expected_assistsper90": ":.2f"
        },
        color_continuous_scale="Viridis",
        title="Top Recruitment Targets",
        labels={
            "expected_assistsper90": "Expected Assists per 90",
            "expected_goalsper90": "Expected Goals per 90",
            "market_value": "Market Value (£)"
        }
    )

# Label each player
    fig.update_traces(
        text=filtered_creators.index,
        textposition="top center",
        marker=dict(line=dict(width=1, color="black"))
    )

# Improve layout
    fig.update_layout(
        template="plotly_white",
        height=700,
        coloraxis_colorbar=dict(title="Market Value (£)")
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Top Performers based on expected stats:")
    st.write("Top 20 Overperformers (Players who have outperformed their expected goals)")
    st.dataframe(top_goal_overperformers[['Comp','Squad','Pos','Age','market_value','Gls_per90','expected_goalsper90','Ast_per90','expected_assistsper90']].sort_values(['Gls_per90','Ast_per90'], ascending=False).head(20))    
    fig, ax = plt.subplots(figsize=(14,8))
    ax.scatter(top_goal_overperformers['expected_goalsper90'], top_goal_overperformers['Gls_per90'], alpha=0.5)
    for i, player in enumerate(top_goal_overperformers.index):
        ax.annotate(player, (top_goal_overperformers['expected_goalsper90'][i], top_goal_overperformers['Gls_per90'][i]),size=10, ha='left', va='bottom')
    ax.set_xlabel("Expected Goals per 90", fontsize=12)
    ax.set_ylabel("Goals per 90", fontsize=12)
    ax.set_title("Overperformers: Goals per 90 vs Expected Goals per 90", fontsize=14)
    st.pyplot(fig)

    st.write("Top 20 creators")
    st.dataframe(top_creators)
    fig, ax = plt.subplots(figsize=(14,8))
    ax.scatter(top_creators['expected_assistsper90'], top_creators['expected_goalsper90'], alpha=0.5)
    for i, player in enumerate(top_creators.index):
        ax.annotate(player, (top_creators['expected_assistsper90'][i], top_creators['expected_goalsper90'][i]),size=10, ha='left', va='bottom')
    ax.set_xlabel("Expected Assists per 90", fontsize=12)
    ax.set_ylabel("Expected Goals per 90", fontsize=12)
    ax.set_title("Overperformers: Expected Assists per 90 vs Expected Goals per 90", fontsize=14)
    st.pyplot(fig)
    
   

