import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture (scope = "session") # т.о. обозначаем пайтесту, что эта функция - фикстура
def app(request):
    fixture = Application() # функция создает (иниц-ет) фикстуру, объект Application, и возвращает ее
    request.addfinalizer(fixture.destroy) # для разрушения фикстуры
    return fixture
