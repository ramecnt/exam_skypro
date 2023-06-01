from dao.birthday_dao import BirthdayDAO


class BirthdayService:

    def __init__(self, dao: BirthdayDAO):
        self.dao = dao

    def get_one(self, nid):
        return self.dao.get_one(nid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data, nid):
        birthday = self.dao.get_one(nid)
        birthday.fio = data.get("fio")
        birthday.preference = data.get('preference')
        self.dao.update(birthday)

    def update_partial(self, data, nid):
        birthday = self.get_one(nid)

        if "fio" in data:
            birthday.fio = data.get("fio")
        if "date_of_birthday" in data:
            birthday.date_of_birthday = data.get("date_of_birthday")
        if "preference" in data:
            birthday.preference = data.get("preference")

        self.dao.update(birthday)

    def delete(self, nid):
        return self.dao.delete(nid)
