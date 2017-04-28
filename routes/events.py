from flask import jsonify
from flask_restful import Resource, reqparse, abort
from entity.events import Events as EventsEntity
from app import db, push, delete, put, patch

parser = reqparse.RequestParser()
parser.add_argument('start')
parser.add_argument('end')
parser.add_argument('title')


def check_if_all_data_exist(args):
    if (args['start'] is None or args['end'] is None or args['title'] is None):
        abort(400, message="All fields have to be filled".args)


def add(args):
    event = EventsEntity(args['start'], args['end'], args['title'])
    push(event)


class Events(Resource):
    def get(self):
        events = EventsEntity.query.all()
        return jsonify([i.serialize() for i in events])

    def post(self):
        args = parser.parse_args()
        check_if_all_data_exist(args)
        add(args)
        return args


class Event(Resource):
    def get(self, id: int):
        event = EventsEntity.query.get(id)
        return jsonify([event.serialize()])

    def put(self, id: int):
        event=db.session.query(EventsEntity).filter_by(id=id)
        args = parser.parse_args()
        check_if_all_data_exist(args)
        put(event,args)
    def delete(self, id: int):
        event = EventsEntity.query.get(id)
        delete(event)

    def patch(self, id: int, name):
        return 'put %d %s' % (id, name)
