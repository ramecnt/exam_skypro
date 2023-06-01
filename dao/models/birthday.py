from setup_db import db
from marshmallow import Schema, fields
import datetime


class Birthday(db.Model):
    """
    Модель для представления информации о дне рождения в базе данных.
    """

    __tablename__ = 'birthday'

    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(1000))
    date_of_birthday = db.Column(db.Date, default=datetime.date.today())
    preference = db.Column(db.String(1000))


class BirthdaySchema(Schema):
    """
    Схема для сериализации и десериализации объектов Birthday.
    """

    id = fields.Int(dump_only=True)
    fio = fields.Str()
    date_of_birthday = fields.DateTime(dump_only=True)
    preference = fields.Str()
