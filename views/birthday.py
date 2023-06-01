from flask import request
from flask_restx import Resource, Namespace
from implemented import birthday_service, birthdays_schema, birthday_schema

birthday_ns = Namespace('birthdays')

@birthday_ns.route('/')
class BirthdaysView(Resource):
    """
    Ресурс для работы со списком дней рождения.
    """

    def get(self):
        """
        Обрабатывает GET-запрос для получения списка всех дней рождения.

        Возвращает:
            - Список дней рождения.
        """
        birthdays = birthday_service.get_all()
        return birthdays_schema.dump(birthdays), 200

    def post(self):
        """
        Обрабатывает POST-запрос для создания нового дня рождения.

        Параметры:
            - data: Данные для создания нового дня рождения.

        Возвращает:
            - Созданный день рождения.
        """
        data = request.json
        new_birthday = birthday_service.create(data)

        return birthday_schema.dump(new_birthday), 201

@birthday_ns.route('/<int:nid>')
class BirthdayView(Resource):
    """
    Ресурс для работы с отдельным днем рождения.
    """

    def get(self, nid):
        """
        Обрабатывает GET-запрос для получения информации о конкретном дне рождения.

        Параметры:
            - nid: Идентификатор дня рождения.

        Возвращает:
            - День рождения.
        """
        birthday = birthday_service.get_one(nid)
        return birthday_schema.dump(birthday), 200

    def put(self, nid):
        """
        Обрабатывает PUT-запрос для обновления информации о конкретном дне рождения.

        Параметры:
            - nid: Идентификатор дня рождения.
            - data: Обновленные данные дня рождения.

        Возвращает:
            - Обновленный день рождения.
        """
        data = request.json
        birthday_service.update(data, nid)

        birthday = birthday_service.get_one(nid)
        return birthday_schema.dump(birthday), 202

    def patch(self, nid):
        """
        Обрабатывает PATCH-запрос для частичного обновления информации о конкретном дне рождения.

        Параметры:
            - nid: Идентификатор дня рождения.
            - data: Частично обновленные данные дня рождения.

        Возвращает:
            - Обновленный день рождения.
        """
        data = request.json
        birthday_service.update_partial(data, nid)

        birthday = birthday_service.get_one(nid)
        return birthday_schema.dump(birthday), 202

    def delete(self, nid):
        """
        Обрабатывает DELETE-запрос для удаления конкретного дня рождения.

        Параметры:
            - nid: Идентификатор дня рождения.

        Возвращает:
            - Результат удаления дня рождения.
        """
        birthday_service.delete(nid)
        response = {"message": "birthday has deleted successfully"}

        return response, 200
