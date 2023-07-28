from flask import Flask
from router_creator import create_router

app = Flask(__name__)
app = create_router(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    #app.run()
