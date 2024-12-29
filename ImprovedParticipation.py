@app.route('/register_participation/<int:event_id>', methods=['POST'])
def register_participation(event_id):
    username = request.form.get('username')
    # Add logic to register user to the event in the database.
    return f"{username} has successfully registered for event ID: {event_id}"

if _name_ == '_main_':
    app.run(debug=True)