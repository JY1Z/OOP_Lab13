#1
from flask import Flask, jsonify
app = Flask(__name__)

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

@app.route('/prime_number/<int:num>')
def check_prime(num):
    is_prime_result = is_prime(num)
    response = {"Number": num, "isPrime": is_prime_result}
    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

#2
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb://root:123456@localhost:3306/airports'
db = SQLAlchemy(app)

class Airport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    icao = db.Column(db.String(4), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

db.create_all()

@app.route('/airport/<icao_code>')
def get_airport_data(icao):
    airport = Airport.query.filter_by(icao=icao.upper()).first()

    if airport:
        response = {"ICAO": airport.icao, "Name": airport.name, "Location": airport.municipality}
    else:
        response = {"error": "Airport not found"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)