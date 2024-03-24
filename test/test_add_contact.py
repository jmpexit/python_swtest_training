# -*- coding: utf-8 -*-
import pytest
from time import sleep
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.session.login(username="admin", passwd="secret")
    app.create_new_contact(Contact(name="U", midname="", surname="Ni", nick="sad", title="ti2", \
                                    co="very big co2", addr="USA, CA, LA, sm.str, smth", hometel="111-11-12",\
                                    mobtel="1-111-111-1112", worktel="222-22-23", fax="222-22-23", email="uu@ex.ca",\
                                    bday="3", bmonth="January", byear="1985", groupname="group1"))
    sleep(30)
    app.session.logout()
