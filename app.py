import random
import string

from flask import Flask, render_template, request, make_response, jsonify
from flask_bootstrap import Bootstrap
import os


app = Flask(__name__)

Bootstrap(app)


# @app.route('/')
# def hello_world():
#     return render_template('base.html')

def success_response(data):
    app.logger.debug('Received Subscribers: ', len(data['mobileNumbers']))
    letters = string.ascii_letters
    token_id = ''.join(random.choice(letters) for i in range(25))
    response = make_response(jsonify(tokenId=token_id), 202)
    return response


def error_response(data):
    return {}


@app.route('/sms/v1/messageContact/Mjo3ODow/send', methods=['GET', 'POST'])
def marketing_cloud_sms():
    if request.method == 'POST':
        data = request.get_json()
        return success_response(data)


if __name__ == '__main__':
    app.run()
