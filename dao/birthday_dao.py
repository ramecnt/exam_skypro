from dao.models.birthday import Birthday


class BirthdayDAO:
    """
    Класс для работы с моделью Birthday в базе данных.
    """

    def __init__(self, session):
        """
        Конструктор класса BirthdayDAO.

        Параметры:
            - session: Объект сеанса работы с базой данных.
        """
        self.session = session

    def get_one(self, nid):
        """
        Получает объект Birthday по его идентификатору.

        Параметры:
            - nid: Идентификатор объекта Birthday.

        Возвращает:
            - Объект Birthday или None, если объект не найден.
        """
        return self.session.query(Birthday).get(nid)

    def get_all(self):
        """
        Получает все объекты Birthday из базы данных.

        Возвращает:
            - Список объектов Birthday.
        """
        return self.session.query(Birthday).all()

    def create(self, data):
        """
        Создает новый объект Birthday в базе данных.

        Параметры:
            - data: Словарь с данными для создания объекта Birthday.

        Возвращает:
            - Созданный объект Birthday.
        """
        birthday = Birthday(**data)

        self.session.add(birthday)
        self.session.commit()

        return birthday

    def update(self, birthday):
        """
        Обновляет существующий объект Birthday в базе данных.

        Параметры:
            - birthday: Объект Birthday для обновления.
        """
        self.session.add(birthday)
        self.session.commit()

    def delete(self, nid):
        """
        Удаляет объект Birthday из базы данных по его идентификатору.

        Параметры:
            - nid: Идентификатор объекта Birthday.
        """
        birthday = self.get_one(nid)

        self.session.delete(birthday)
        self.session.commit()
