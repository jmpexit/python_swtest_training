# -*- coding: utf-8 -*-
from time import sleep
from model.contact import Contact

def test_update_contact(app):
    app.open_home_page()
    app.contact.update_some(Contact(name="Uuu", midname="Mm", surname="Niiiiiii", nick="pinky", title="ti3", \
                                    co="very big co3", addr="USA, NY, B, sm.str, smth", hometel="111-11-13",\
                                    mobtel="1-111-111-1113", worktel="888-22-23", fax="888-22-23", email="uum@ex.ny",\
                                    bday="5", bmonth="January", byear="1986", groupname="group1"))
    sleep(5)
