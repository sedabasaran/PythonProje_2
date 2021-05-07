import requests,time,datetime,json 
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/alotech", methods=["GET", "POST" ])
def alotech():
    if request.method == "GET":
        return "Anasayfa. "
    else:
        req = requests.get('https://staging1.alo-tech.com/api/?function=reportsCDRLogs&startdate=2017-08-01%2012:00:00&finishdate=2017-08-04%2013:00:00&app_token=ag9zfnRlbGVmb25pLXRlc3RyHwsSElRlbmFudEFwcGxpY2F0aW9ucxiAgICw46OcCQyiARVzdGFnaW5nMS5hbG8tdGVjaC5jb20')
        data = json.loads(req.content)
        return render_template('alotech.html',data=data['CallList'])

if __name__ == "__main__":
    app.run(host = "127.0.0.1",port=8080,debug=True)