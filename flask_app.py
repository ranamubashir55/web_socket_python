from flask import Flask, render_template, request
from flask_socketio import SocketIO
import time, json
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def my():
    return render_template("index.html")



def test():
    c=0
    while True:
        time.sleep(3)
        c=c+1
        yield {"data":c}
        
def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@app.route("/login")
def log():
    return "logged in successfully"

@socketio.on('evt')
def api(message, methods=['GET', 'POST']):
    data = json.loads(message)
    print(data)
    for x in test():
        socketio.emit('update', x, callback=messageReceived)
    

# @socketio.on('connect')
# def handle_my_custom_event():
#     print("client connected")
#     a=[]
#     for x in test():
#         # a.append(x)
#         print(x)
#         socketio.emit('getallonlinestoresres', x, callback=messageReceived)
#         # print("ddddddddddd")
        
# @socketio.on('my_event')
# def handle2_my_custom_event(json):
#     print('received json: ' + str(json))




# connected_stores = [1,2,3]

# @socketio.on('connect')
# def connect():
#     socketio.emit('getallonlinestoresres', connected_stores, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0" , port=8080, debug=True)