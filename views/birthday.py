from flask import request
from flask_restx import Resource, Namespace
from implemented import birthday_service, birthdays_schema, birthday_schema


birthday_ns = Namespace('birthdays')


@birthday_ns.route('/')
class BirthdaysView(Resource):

    def get(self):
        birthdays = birthday_service.get_all()
        return birthdays_schema.dump(birthdays), 200

    def post(self):
        data = request.json
        new_birthday = birthday_service.create(data)

        return birthday_schema.dump(new_birthday), 201


@birthday_ns.route('/<int:nid>')
class BirthdayView(Resource):

    def get(self, nid):
        birthday = birthday_service.get_one(nid)
        return birthday_schema.dump(birthday), 200

    def put(self, nid):
        data = request.json
        birthday_service.update(data, nid)

        birthday = birthday_service.get_one(nid)

        return birthday_schema.dump(birthday), 202

    def patch(self, nid):
        data = request.json
        birthday_service.update_partial(data, nid)

        birthday = birthday_service.get_one(nid)

        return birthday_schema.dump(birthday), 202

    def delete(self, nid):
        birthday_service.delete(nid)
        response = {"message": "birthday has deleted successfully"}

        return response, 200
