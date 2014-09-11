# Flask SocketIO Example

This repo provides a working example of web socket communication between a client and server.

The server is a Python Flask/Greenlet web server and the client is a simple html page using the SocketIO js library.

It demonstrates the following:

* A simple flask route response with the index.html page.

	@app.route('/')
	def index():
	    
	    print 'Client hitting the index page.'
	    return render_template('index.html')


* The establishment of a websocket connection, during which the server prints
  as a sanity check and sends (emits) some data to the client under the 'my response' event type.

	@socketio.on('connect', namespace='/test')
	def test_connect():
	    print 'Server received start of connection from client.'
	    emit('my response', {'data': 'Connected', 'count': 0})

* A client button click that calls a js function which emits back to the server under the event type
  'start_event_processor'. This is received by the server, which prints to prove it's working. The
  server also emits back to the client, as an acknowledgment.
  
* The use of a specific namespace to manage messages to and from the server.

