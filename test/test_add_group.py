# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture # т.о. обозначаем пайтесту, что эта функция - фикстура
def app(request):
    fixture = Application() # функция создает (иниц-ет) фикстуру, объект Application, и возвращает ее
    request.addfinalizer(fixture.destroy) # для разрушения фикстуры
    return fixture


def test_add_group(app): #тест.метод принимает фикстуру в кач. пар-ра
    app.login(username="admin", passwd="secret")
    app.create_new_group(Group(name="group2", header="group header 2", footer="group footer 2"))
    app.logout()
