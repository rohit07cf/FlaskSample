
# coding: utf-8

# In[ ]:


#Flask Imports
from flask import Flask
from flask import jsonify
from flask import request


# In[ ]:


app=Flask(__name__)


# In[ ]:


@app.route("/")
def hello12():
    return "Hello World!"


# In[ ]:


@app.route('/getRequest', methods=['get'])
def create_cm():
    summary = request.args.get('summary', None) # use default value repalce 'None'
    change = request.args.get('change', None)
    # do something, eg. return json response
    return jsonify({'summary': summary, 'change': change})


# In[ ]:


@app.route('/getPostParameters',methods=['POST'])
def calculateModelAccuracyNew():
    #Mandatory Params
    name=request.form['name'];
    age=request.form['age']
    #Optional Params
    address=request.form.get('address')
    finalStr="Name:"+name+" Age:"+age+" Address:"+str(address)
    return finalStr;


# In[ ]:


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


# In[ ]:


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


# In[ ]:


if __name__ == "__main__":
    app.run(app.run(host='0.0.0.0', port=8084))

