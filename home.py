def get_api_info():
    my_dict = {
        'url1': 'http://127.0.0.1:5000/',
        'url2': 'http://127.0.0.1:5000/history',
        'url3': 'http://127.0.0.1:5000/api/teams',
        'url4': "http://127.0.0.1:5000/api/teamvsteam?team1=Rajasthan%20Royals&team2=Royal%20Challengers%20Bangalore",
        'url5': "http://127.0.0.1:5000/api/bowlers",
        'url6': "http://127.0.0.1:5000/api/batsmen",
        'url7': 'http://127.0.0.1:5000/api/batsmanrecord?batsman=V%20Kholi',
        'url8': 'http://127.0.0.1:5000/api/bowling-record?bowler=Mohammed%20Shami'
    }

    text = """I created this API to provide various types of information.
    You can fetch data using the provided API URLs. Here are some sample URLs:
    - Fetch history: {url2}
    - Fetch teams: {url3}
    - Fetch team vs team: {url4}
    - Fetch bowlers: {url5}
    - Fetch batsmen: {url6}
    - Fetch batsman record: {url7}
    - Fetch bowling record: {url8}
    """.format(**my_dict)

    return my_dict, text



