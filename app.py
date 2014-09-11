#import time
#from threading import Thread
from flask import Flask, render_template, session, request
from flask.ext.socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.debug = False
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    
    print 'Client hitting the index page.'
    return render_template('index.html')

# -----------------------------------------------------------------------------

@socketio.on('start_processor_event', namespace='/test')
def start_processor_event(data):
    """ Event receiver that starts the processor """
    
    print 'Server received a start command from the client button press'
    print 'Server received data received from client \n %s'%(data['data'])
    socketio.emit('my response', {'data': "Content emitted from server."}, namespace='/test')
    
# -----------------------------------------------------------------------------
         
@socketio.on('connect', namespace='/test')
def test_connect():
    print 'Server received start of connection from client.'
    emit('my response', {'data': 'Connected', 'count': 0})
    

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print 'Server and client disconnected.'


if __name__ == '__main__':
    
    print '>> Starting the Flask Websocket server.'
    socketio.run(app)
    #main()