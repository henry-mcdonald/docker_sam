from flask import Flask, request

from datetime import datetime
import os
import json

from samlogic import get_response


app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def entry_point():
    #return "hello"
    if request.method == 'POST':
        #response = getSamsResponse()
        try:
            return get_response(request.form.get('userinput'))
        except Exception as e:
            return str(e)
    elif request.method == 'GET':
        now = datetime.now()
        return f'Thanks for the GET request.. current time is like {now}'

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0',port=port)