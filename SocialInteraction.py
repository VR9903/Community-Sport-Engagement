@app.route('/comment_on_event/<int:event_id>', methods=['POST'])
def comment_on_event(event_id):
    comment_text = request.form.get('comment_text')
    # Here, you'd save the comment to the database.
    return f"Your comment: '{comment_text}' has been posted for event ID: {event_id}"