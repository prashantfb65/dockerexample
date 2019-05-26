# compose_flask/app.py
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    resp_back = f"<h1> Innovation Website visited {int(redis.get('hits'))} time(s) </h1>"
    return resp_back


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
