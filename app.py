from flask import Flask
import redis

app = Flask(__name__)
#connect to redis server first
redis_server = redis.Redis(host ="redis", port = 6379)

@app.route('/')
def hello_world():
    return 'CoderCo Containers Session!'

@app.route('/count')
def count():
    #use redis to increment and display count 

    timesvisited = redis_server.incr("visits")

    return f"the website has been visited: {timesvisited} times"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)