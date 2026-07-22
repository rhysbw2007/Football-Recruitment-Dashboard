import matplotlib.pyplot as plt
import seaborn as sns

from data import (top10_finishers, top20_assisters, top20_scorers)

def plot_top_finishers(top10_finishers):
    plt.figure(figsize=(8,6))
    sns.scatterplot(data=top10_finishers, x='Sh/90', y ='Gls_per90', hue="Player")
    plt.xlabel("Shots per 90")
    plt.ylabel("Goals per 90")
    plt.title("Scatter plot of europes top 10 best finisher based on goals per 90 against shots per 90")
    plt.show()

def plot_top_assisters(top20_assisters):
    plt.figure(figsize=(8,6))
    sns.barplot(data=top20_assisters, x=top20_assisters.index, y="Ast_per90")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Assists per 90")
    plt.title("Top 20 Assisters")
    plt.show()

def plot_top_scorers(top20_scorers):
    plt.figure(figsize=(8,6))
    sns.barplot(data=top20_scorers, x="Player", y="Gls_per90")
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Goals per 90")
    plt.title("Top 20 scorers")
    plt.show()
