# -*- coding: utf-8 -*-
import pytest
from time import sleep
from group import Group
from contact import Contact
from application import Application


@pytest.fixture # т.о. обозначаем пайтесту, что эта функция - фикстура
def app(request):
    fixture = Application() # функция создает (иниц-ет) фикстуру, объект Application, и возвращает ее
    request.addfinalizer(fixture.destroy) # для разрушения фикстуры
    return fixture


def test_add_group(app): #тест.метод принимает фикстуру в кач. пар-ра (фикстура передается в тест. ф-ию)
    app.login(username="admin", passwd="secret")
    app.create_new_group(Group(name="group3", header="group header 3", footer="group footer 3"))
    app.logout()

def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", passwd="secret")
    app.create_new_contact(Contact(name="U", midname="", surname="Ni", nick="sad", title="ti2", \
                                    co="very big co2", addr="USA, CA, LA, sm.str, smth", hometel="111-11-12",\
                                    mobtel="1-111-111-1112", worktel="222-22-23", fax="222-22-23", email="uu@ex.ca",\
                                    bday="3", bmonth="January", byear="1985", group="group1"))
    sleep(30)
    app.logout()
