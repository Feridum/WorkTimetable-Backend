from flask import Flask, Blueprint

app = Flask(__name__)
app.debug = True


api = Blueprint('api',__name__)

@api.route('/')
def hello_world():
    return 'Hello world!'

app.register_blueprint(api,url_prefix="/api")
if __name__ == '__main__':
    app.run()
