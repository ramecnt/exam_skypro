from dao.birthday_dao import BirthdayDAO
from dao.models.birthday import BirthdaySchema
from services.birthday_service import BirthdayService
from setup_db import db

birthday_dao = BirthdayDAO(db.session)
birthday_service = BirthdayService(dao=birthday_dao)

birthday_schema = BirthdaySchema()
birthdays_schema = BirthdaySchema(many=True)
