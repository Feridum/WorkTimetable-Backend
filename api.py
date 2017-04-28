from flask_restful import Resource, Api
from routes.events import Events,Event
from app import app

api = Api(app)

class Index(Resource):
    def get(self):
        return {self.representations}

api.add_resource(Index, '/api')
api.add_resource(Event,'/api/event/<int:id>', '/api/event/<int:id>/<name>')
api.add_resource(Events,'/api/events')

if __name__ == '__main__':
    app.run(debug=True)
