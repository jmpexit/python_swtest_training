# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app): #тест.метод принимает фикстуру в кач. пар-ра
    app.session.login(username="admin", passwd="secret")
    app.group.create(Group(name="group3", header="group header 3", footer="group footer 3"))
    app.session.logout()
