import pytest
from model.group import Group
from fixture.application import Application

fixture = None
@pytest.fixture # т.о. обозначаем пайтесту, что эта функция - фикстура
def app(request):
    global fixture
    if fixture is None:
        fixture = Application() # функция создает (иниц-ет) фикстуру, объект Application, и возвращает ее
        fixture.session.login(username="admin", passwd="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin", passwd="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)  #отдельная фикстура для финализации
                                        # autouse=True означает, что фикстура сработает автоматически,
                                        #несмотря на то, что не указана ни в одном из тестов
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin) # для разрушения фикстуры
    return fixture
