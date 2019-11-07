from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'toBeFilledInLater'
socket_io = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('session.html')


def message_received():
    print('message was received!!!')


@socket_io.on('my event')
def handle_my_custom_event(json):
    print('received my event: ' + str(json))
    socket_io.emit('my response', json, callback=message_received)


if __name__ == '__main__':
    socket_io.run(app, debug=True)

