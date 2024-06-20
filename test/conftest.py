import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture (scope = "session") # т.о. обозначаем пайтесту, что эта функция - фикстура
def app(request):
    fixture = Application() # функция создает (иниц-ет) фикстуру, объект Application, и возвращает ее
    fixture.session.login(username="admin", passwd="secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin) # для разрушения фикстуры
    return fixture
