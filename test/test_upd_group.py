# -*- coding: utf-8 -*-
from model.group import Group

def test_update_group(app): #тест.метод принимает фикстуру в кач. пар-ра
    app.group.update_first_group(Group(name="group3", header="group header 333", footer="group footer 333"))

def test_update_group_name(app):
    app.group.update_first_group(Group(name="group3"))

def test_update_group_header(app):
    app.group.update_first_group(Group(header="group header 333"))

def test_update_group_footer(app):
    app.group.update_first_group(Group(footer="group footer 333"))