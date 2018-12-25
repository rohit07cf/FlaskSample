#Flask Imports
from flask import Flask
from flask import jsonify
from flask import request

app=Flask(__name__)

@app.route("/")
def hello12():
    return "Hello World!"

#localhost:8084/getRequest?summary=Param1&change=Param2
@app.route('/getRequest', methods=['get'])
def create_cm():
    summary = request.args.get('summary', None) # use default value repalce 'None'
    change = request.args.get('change', None)
    # do something, eg. return json response
    return jsonify({'summary': summary, 'change': change})



@app.route('/getPostParameters',methods=['POST'])
def calculateModelAccuracyNew():
    #Mandatory Params
    name=request.form['name'];
    age=request.form['age']
    #Optional Params
    address=request.form.get('address')
    finalStr="Name:"+name+" Age:"+age+" Address:"+str(address)
    return finalStr;

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run(app.run(host='0.0.0.0', port=8084))

