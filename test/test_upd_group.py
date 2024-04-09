# -*- coding: utf-8 -*-
from model.group import Group

def test_update_group(app): #тест.метод принимает фикстуру в кач. пар-ра
    app.session.login(username="admin", passwd="secret")
    app.group.update_first(Group(name="group3", header="group header 333", footer="group footer 333"))
    app.session.logout()
