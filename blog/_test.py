import json
from datetime import datetime as dt
from datetime import timedelta
import requests
import base64
from werkzeug.security import generate_password_hash, check_password_hash



pw = ''
hsh = generate_password_hash(pw, method="pbkdf2:sha256", salt_length=8)
print(hsh)

print(check_password_hash(hsh, pw))


# from flask import Flask, request, jsonify

# app = Flask(__name__)


# auth_cyph = "bXlzaGtpbnM6d29yZHBhc3M="
# decyph = base64.b64decode(auth_cyph).decode("utf-8")
# print(decyph)

