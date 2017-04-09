from flask import Blueprint

event = Blueprint('event', __name__)


@event.route('/')
def get_events():
    return 'get'


@event.route('/<name>', methods=['POST'])
def post_events(name):
    return name

@event.route('/<int:id>', methods=['PUT'])
def put_events(id):
    return 'put %d '% id

@event.route('/<int:id>', methods=['DELETE'])
def delete_events(id):
    return 'delete %d '% id

@event.route('/<int:id>/<name2>', methods=['PATCH'])
def patch_events(id,name2):
    return 'put %d %s' % (id,name2)