from flask import Flask, jsonify, request, json
import ipl
import numpy as np
from history import add_to_history, get_history
import bowler
import batsman
import home

app = Flask(__name__)


@app.before_request
def add_request_to_history():
    url = request.url
    query = f"{request.path}?{request.query_string.decode()}"
    add_to_history(url, query, None)



@app.route('/')
def home_():
    api_dict, api_text = home.get_api_info()

    # Format the text using HTML
    formatted_text = "<h1>Welcome to My API</h1><p>{}</p>".format(api_text.replace('\n', '<br>'))
    return formatted_text


@app.route('/api/teams')
def all_teams():
    teams = ipl.all_teams()
    return jsonify(teams)


@app.route("/api/teamvsteam")
def teamvsteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    # Assuming ipl.team_vs_team returns a dictionary with int64 values
    res = ipl.team_vs_team(team1, team2)

    # Convert int64 values in the dictionary to int
    for key, value in res.items():
        if isinstance(value, np.int64):
            res[key] = int(value)

    return jsonify(res)



@app.route('/api/team_record')
def team_record():
    team = request.args.get('team')
    response = ipl.teamAPI(team)
    return response


@app.route('/api/batsmanrecord')
def batsman_record():
    batter_name = request.args.get('batsman')
    result = ipl.batsmanAPI('batter_name')
    return result

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = ipl.bowlerAPI(bowler_name)
    return response

@app.route('/history')
def view_history():
    history = get_history()
    return jsonify(history)

@app.route('/api/bowlers')
def get_all_bowlers():
    response = bowler.all_ipl_bowler()
    return response

@app.route('/api/batsmen')
def get_all_batsmen():
    response = batsman.all_ipl_batsman()
    return jsonify(response)




app.run(debug=True)
