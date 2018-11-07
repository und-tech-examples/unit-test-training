import pytest

from python.services.user import UserService


class TestUser:
    url = None
    mock = None

    @classmethod
    def setup_class(cls):
        cls.service = UserService()
        cls.mock = [
            {'id': 1, 'name': 'foo'},
            {'id': 2, 'name': 'bar'},
            {'id': 3, 'name': 'test_user'}
        ]

    def test_create(self):
        id = self.service.create(name=self.mock[2]['name'])
        assert id is not None

    @pytest.mark.dependency(depends=['test_create'])
    def test_list(self):
        assert self.service.list() == self.mock

    @pytest.mark.dependency(depends=['test_list'])
    def test_list_by_id(self):
        assert self.service.list_by_id(self.mock[2]['id']) == self.mock[2]

    @pytest.mark.dependency(depends=['test_list_by_id'])
    def test_update(self):
        response = self.service.update(self.mock[2]['id'], name=self.mock[0]['name'])
        assert response['id'] == self.mock[2]['id'] and response['name'] == self.mock[0]['name']

    @pytest.mark.dependency(depends=['test_update'])
    def test_delete(self):
        assert self.service.delete(self.mock[2]['id']) == {}
