# -*- coding: utf-8 -*-
from model.group import Group

def test_update_group(app): #тест.метод принимает фикстуру в кач. пар-ра
    app.session.login(username="admin", passwd="secret")
    app.group.update_first(Group(name="group111", header="group header 111", footer="group footer 111"))
    app.session.logout()
