from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import mysql.connector
import hashlib

mysql_connection = mysql.connector.connect(host="localhost",
                                           user="root",
                                           password="ram28873",
                                           database="online_election_system_se")

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["JWT_SECRET_KEY"] = "this-is-a-secret"
jwt = JWTManager(app)

salt = 123456


def verify_voter_login(voter_id, password):
    cursor = mysql_connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM VOTER WHERE voter_id = '{voter_id}'")
    results = cursor.fetchall()
    hashed_password = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        str(salt).encode("utf-8"),
        100000
    )
    print(results)


verify_voter_login('ABC1234567', 'sjkjfksj')


@app.route('/voterlogin', methods=["POST"])
def voter_login():
    recvd_json = request.get_json()
    user_voter_id = recvd_json['voter_id']
    user_password_id = recvd_json['password']
