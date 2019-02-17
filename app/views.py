from flask import Flask, request, jsonify
from app.users.users import Users
from passlib.hash import sha256_crypt


app = Flask(__name__)

usersInstance = Users()


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    data = request.get_json()
    username = data['username']
    password = data['password']
    encrypted_password = sha256_crypt.encrypt(password)
    usersInstance.signup(username, encrypted_password)
    return jsonify({'msg': 'Done signing up'}), 201
