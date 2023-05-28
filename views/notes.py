from flask import request, jsonify
from flask_restx import Resource, Namespace
from dao.models.note import NoteSchema
from implemented import note_service


note_ns = Namespace('notes')

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)


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
        updated_note = note_service.update(data, nid)

        return note_schema.dump(updated_note), 204

    def patch(self, nid):
        data = request.json
        updated_note = note_service.update_partial(data, nid)

        return note_schema.dump(updated_note), 204

    def delete(self, nid):
        note_service.delete(nid)
        response = {"status": 204}

        return jsonify(response), 204
