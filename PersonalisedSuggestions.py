from flask import Flask, render_template, request
import random

app = Flask(_name_)

# Example user data (this would be in a database in a real app)
users = {
    'user1': ['basketball', 'soccer'],
    'user2': ['baseball', 'volleyball'],
    'user3': ['basketball', 'tennis']
}

events = [
    {'event_name': 'Basketball Tournament', 'category': 'basketball'},
    {'event_name': 'Soccer League', 'category': 'soccer'},
    {'event_name': 'Baseball Championship', 'category': 'baseball'},
    {'event_name': 'Volleyball Match', 'category': 'volleyball'},
    {'event_name': 'Tennis Open', 'category': 'tennis'},
]

@app.route('/suggest_events/<username>', methods=['GET'])
def suggest_events(username):
    user_interests = users.get(username, [])
    recommended_events = [event for event in events if event['category'] in user_interests]
    
    return render_template('suggestions.html', events=recommended_events)

if _name_ == '_main_':
    app.run(debug=True)