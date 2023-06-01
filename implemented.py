from dao.birthday_dao import BirthdayDAO
from dao.models.birthday import BirthdaySchema
from services.birthday_service import BirthdayService
from setup_db import db

""" Имплементация классов в экземляры для будущео использования """

birthday_dao = BirthdayDAO(db.session)
birthday_service = BirthdayService(dao=birthday_dao)

""" Имплеметация классов в экземаляры для сериализации """

birthday_schema = BirthdaySchema()
birthdays_schema = BirthdaySchema(many=True)
