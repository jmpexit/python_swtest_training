# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app): #тест.метод принимает фикстуру в кач. пар-ра
    app.group.create(Group(name="group3", header="group header 3", footer="group footer 3"))

def test_add_empty_group(app): #тест.метод принимает фикстуру в кач. пар-ра
    app.group.create(Group(name="empty_group", header="", footer=""))