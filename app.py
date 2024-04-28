from flask import Flask, request
from flask import render_template
from flask import jsonify
import random

home_data = {'kitchen': {'light': False, 'temp': 22.3, 'brightness': 0, },
             'bathroom': {'light': False, 'temp': 20.4, 'brightness': 0, },
             'hallway': {'light': False, 'temp': 19.3, 'brightness': 0, },
             'bedroom': {'light': False, 'temp': 21.3, 'brightness': 0, },
             'balcony': {'light': False, 'temp': 14.0, 'brightness': 0, },
             }

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html", **home_data)


@app.route('/<room>/<device>/<action>', methods=['GET', 'POST'])
def proceed(room, device, action):
    global home_data
    if request.method == 'GET':
        match device:
            case 'light':
                match action:
                    case 'toggle':
                        home_data[room]['light'] = not (home_data[room]['light'])
                        print(f'Changed {device} in {room} to {home_data[room][device]}')
                        return jsonify({'state': home_data[room]['light']})
            case 'temp':
                match action:
                    case 'update':
                        temp = {}
                        for room in home_data:
                            home_data[room]['temp'] = home_data[room]['temp'] + random.random()/2
                            temp[room+"Temp"] = home_data[room]['temp']
                            print(f'Changed {device} in {room} to {home_data[room][device]}')
                        return jsonify(temp)

    if request.method == 'POST':
        match device:
            case 'light':
                match action:
                    case 'brightness':
                        home_data[room]['brightness'] = int(request.form.get('brightness'))
                        print(f'Changed {device} in {room} to {home_data[room][action]}')
                        return jsonify({'brightness': home_data[room]['brightness']})




if __name__ == '__main__':
    app.run(host="0.0.0.0")
