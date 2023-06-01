from setup_db import db
from marshmallow import Schema, fields
import datetime

class Birthday(db.Model):
    __tablename__ = 'birthday'

    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(1000))
    date_of_birthday = db.Column(db.Date, default=datetime.date.today())
    preference = db.Column(db.String(1000))


class BirthdaySchema(Schema):
    id = fields.Int(dump_only=True)
    fio = fields.Str()
    date_of_birthday = fields.DateTime(dump_only=True)
    preference = fields.Str()