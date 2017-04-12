from flask import Flask, Blueprint
from flask_restful import Resource, Api
from routes.events import Events

app = Flask(__name__)


api = Api(app)

class Index(Resource):
    def get(self):
        return {self.representations}

api.add_resource(Index, '/api')
api.add_resource(Events,'/api/events', '/api/events/<name>', '/api/events/<int:id>', '/api/events/<int:id>/<name>')

if __name__ == '__main__':
    app.run(debug=True)
