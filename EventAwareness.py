from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(_name_)

# Configuring Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/notify_event', methods=['POST'])
def notify_event():
    event_name = request.form.get('event_name')
    event_date = request.form.get('event_date')
    recipient_list = ['community_member1@example.com', 'community_member2@example.com']

    subject = f"Upcoming Event: {event_name} on {event_date}"
    body = f"Hello! Don't miss the upcoming sports event: {event_name}. Mark your calendars for {event_date}."

    with app.app_context():
        for recipient in recipient_list:
            msg = Message(subject, sender='your-email@gmail.com', recipients=[recipient])
            msg.body = body
            mail.send(msg)
    
    return 'Notifications sent successfully'

if _name_ == '_main_':
    app.run(debug=True)