from dao.birthday_dao import BirthdayDAO


class BirthdayService:
    """
    Класс для предоставления сервисных операций над объектами Birthday.
    """

    def __init__(self, dao: BirthdayDAO):
        """
        Конструктор класса BirthdayService.

        Параметры:
            - dao: Объект BirthdayDAO для доступа к базе данных.
        """
        self.dao = dao

    def get_one(self, nid):
        """
        Получает объект Birthday по его идентификатору.

        Параметры:
            - nid: Идентификатор объекта Birthday.

        Возвращает:
            - Объект Birthday или None, если объект не найден.
        """
        return self.dao.get_one(nid)

    def get_all(self):
        """
        Получает все объекты Birthday.

        Возвращает:
            - Список объектов Birthday.
        """
        return self.dao.get_all()

    def create(self, data):
        """
        Создает новый объект Birthday.

        Параметры:
            - data: Словарь с данными для создания объекта Birthday.

        Возвращает:
            - Созданный объект Birthday.
        """
        return self.dao.create(data)

    def update(self, data, nid):
        """
        Обновляет существующий объект Birthday.

        Параметры:
            - data: Словарь с данными для обновления объекта Birthday.
            - nid: Идентификатор объекта Birthday, который требуется обновить.
        """
        birthday = self.dao.get_one(nid)
        birthday.fio = data.get("fio")
        birthday.preference = data.get('preference')
        self.dao.update(birthday)

    def update_partial(self, data, nid):
        """
        Частично обновляет существующий объект Birthday.

        Параметры:
            - data: Словарь с данными для обновления объекта Birthday.
            - nid: Идентификатор объекта Birthday, который требуется обновить.
        """
        birthday = self.get_one(nid)

        if "fio" in data:
            birthday.fio = data.get("fio")
        if "date_of_birthday" in data:
            birthday.date_of_birthday = data.get("date_of_birthday")
        if "preference" in data:
            birthday.preference = data.get("preference")

        self.dao.update(birthday)

    def delete(self, nid):
        """
        Удаляет объект Birthday по его идентификатору.

        Параметры:
            - nid: Идентификатор объекта Birthday, который требуется удалить.

        Возвращает:
            - Результат удаления объекта.
        """
        return self.dao.delete(nid)
