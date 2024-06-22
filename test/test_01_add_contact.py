# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.open_home_page()
    app.contact.create(Contact(name="Uu", midname="M", surname="Nii", nick="pinky", title="ti3", \
                                    co="very big co3", addr="USA, NY, B, sm.str, smth", hometel="111-11-13",\
                                    mobtel="1-111-111-1113", worktel="222-22-23", fax="222-22-23", email="uum@ex.ny",\
                                    bday="5", bmonth="January", byear="1986", groupname="group3"))