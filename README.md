# ⚽ Football Recruitment Dashboard

An interactive football recruitment dashboard built using **Python**, **Streamlit**, **Pandas**, and **Plotly** to analyse player performance and support data-driven recruitment decisions.

The dashboard combines player statistics, expected performance metrics and market values to help identify potential transfer targets based on positional requirements and budget constraints.

## Features

* Interactive Streamlit dashboard
* Player profile explorer
* League and nationality filters
* Top scorers and assist providers
* Advanced attacking metrics
* Recruitment page with:

  * Budget filter
  * Position filter
  * Market value integration
  * Expected Goals (xG) and Expected Assists (xA) analysis
* Interactive visualisations
* Player comparison functionality

## Technologies

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* Matplotlib
* Seaborn

## Dataset

The dashboard analyses player performance from Europe's top leagues using statistics including:

* Goals
* Assists
* Minutes played
* Expected Goals (xG)
* Expected Assists (xA)
* Market Value
* Position
* Club
* League

## Project Structure

```text
FootballRecruitmentDashboard/
│
├── app.py
├── data.py
├── plots.py
├── requirements.txt
├── README.md
│
└── Data/
```

## Installation

```bash
git clone https://github.com/yourusername/FootballRecruitmentDashboard.git

cd FootballRecruitmentDashboard

pip install -r requirements.txt

streamlit run app.py

You will need to change the filepaths inside data.py once you download the data
```

## Future Improvements

* Recruitment scoring model
* Radar chart comparisons
* Percentile rankings
* League benchmarking
* Similar player recommendations
* Enhanced filtering options
* Team-level analysis

## Skills Demonstrated

* Data cleaning and transformation
* Exploratory data analysis
* Statistical feature engineering
* Interactive dashboard development
* Data visualisation
* Football analytics
* Python application development
