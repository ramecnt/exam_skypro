from dao.models.birthday import Birthday


class BirthdayDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, nid):
        return self.session.query(Birthday).get(nid)

    def get_all(self):
        return self.session.query(Birthday).all()

    def create(self, data):
        birthday = Birthday(**data)

        self.session.add(birthday)
        self.session.commit()

        return birthday

    def update(self, birthday):
        self.session.add(birthday)
        self.session.commit()

    def delete(self, nid):
        birthday = self.get_one(nid)

        self.session.delete(birthday)
        self.session.commit()
