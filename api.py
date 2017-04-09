from flask import Flask, Blueprint
from routes.events import event
app = Flask(__name__)
app.debug = True


api = Blueprint('api',__name__)

@api.route('/')
def hello_world():
    return 'Hello world!'

app.register_blueprint(api,url_prefix="/api")
app.register_blueprint(event,url_prefix="/api/events")

if __name__ == '__main__':
    app.run()
