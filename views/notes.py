from flask import request
from flask_restx import Resource, Namespace
from implemented import note_service, note_schema, notes_schema


note_ns = Namespace('notes')


@note_ns.route('/')
class NotesView(Resource):

    def get(self):
        notes = note_service.get_all()
        return notes_schema.dump(notes), 200

    def post(self):
        data = request.json
        new_note = note_service.create(data)

        return note_schema.dump(new_note), 201


@note_ns.route('/<int:nid>')
class NoteView(Resource):

    def get(self, nid):
        note = note_service.get_one(nid)
        return note_schema.dump(note), 200

    def put(self, nid):
        data = request.json
        note_service.update(data, nid)

        note = note_service.get_one(nid)

        return note_schema.dump(note), 202

    def patch(self, nid):
        data = request.json
        note_service.update_partial(data, nid)

        note = note_service.get_one(nid)

        return note_schema.dump(note), 202

    def delete(self, nid):
        note_service.delete(nid)
        response = {"message": "Note has deleted successfully"}

        return response, 200
