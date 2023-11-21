from flask import Flask
from sys import argv
app = Flask(__name__)
@app.route("/")
def index():
    return "Calculate point total"
@app.route("/calc/<status>/<pointTotal>/<points>")
def calcTotal(status, pointTotal, points):
    if status == "Complete" or status == "Not Earned":
        newTotal = int(pointTotal) + int(points)
    else:
        newTotal = int(pointTotal) - int(points)
    return str(pointTotal if newTotal < 0 else newTotal)
if __name__ == "__main__":
    if len(argv) <= 1:
    	app.run(host = "127.0.0.1", port=56789)
    else:
    	app.run(host = "127.0.0.1", port=int(argv[1])
