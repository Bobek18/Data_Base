from app.dao.alertcontacts_dao import AlertContactsDAO

class AlertContactsService:
    _dao = AlertContactsDAO()

    def find_all(self):
        return self._dao.find_all()

    def find_by_id(self, key: int):
        return self._dao.find_by_id(key)

    def create(self, obj):
        return self._dao.create(obj)

    def create_all(self, obj_list):
        return self._dao.create_all(obj_list)

    def update(self, key: int, new_obj):
        self._dao.update(key, new_obj)

    def patch(self, key: int, field_name, value):
        self._dao.patch(key, field_name, value)

    def delete(self, key: int):
        self._dao.delete(key)

    def delete_all(self):
        self._dao.delete_all()
