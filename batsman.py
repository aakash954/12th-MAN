import pandas as pd
import numpy as np
import json


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)


# Read CSV files and perform necessary operations
matches = pd.read_csv('ipl-matches.csv')
balls = pd.read_csv('IPL_Ball_by_Ball_2008_2022 - IPL_Ball_by_Ball_2008_2022.csv')
balls_matches = pd.merge(matches, balls, on='ID', how='inner')


def all_ipl_batsman():
    seasonwise_batsman = {}
    all_batsman = list(set(balls['batter']))
    season = list(matches['Season'].unique())
    for i in season:
        filtered_data = balls_matches.loc[balls_matches['Season'] == i]
        seasonwise_batsman[i] = list((filtered_data['batter'].unique()))
    result = {
        'total': len(all_batsman),
        'all_batsman_ipl': all_batsman,
        'seasons': season,
        'seasonwise_batsmen': seasonwise_batsman
    }
    return json.dumps(result, cls=NpEncoder)


