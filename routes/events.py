
from flask_restful import Resource


class Events(Resource):
    def get(self):
        return 'get'

    def post(self, name):
        return name

    def put(self, id: int):
        return 'put %d ' % id

    def delete(self, id: int):
        return 'delete %d ' % id

    def patch(self, id: int, name):
        return 'put %d %s' % (id, name)
