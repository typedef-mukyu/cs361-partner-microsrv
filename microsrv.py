from flask import Flask
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
    app.run(host = "127.0.0.1", port=56789)
