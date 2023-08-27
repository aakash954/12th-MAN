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

matches = pd.read_csv('ipl-matches.csv')
balls = pd.read_csv('IPL_Ball_by_Ball_2008_2022 - IPL_Ball_by_Ball_2008_2022.csv')
all_bowler = list(set(balls['bowler']))
balls_matches = pd.merge(matches, balls, on='ID', how='inner')


def all_ipl_bowler():
    seasonwise_bowler = {}
    all_bowler = list(set(balls['bowler']))
    season = list(matches['Season'].unique())
    total = len(all_bowler)
    for i in season:
        filtered_data = balls_matches.loc[balls_matches['Season'] == i]
        seasonwise_bowler[i] = list((filtered_data['bowler'].unique()))
    new_dict = {
        'total': total,
        'all_bolwer_ipl': all_bowler,
        'seasons': season,
        'seasonwise_bowlers': seasonwise_bowler

    }
    return json.dumps(new_dict, cls=NpEncoder)

