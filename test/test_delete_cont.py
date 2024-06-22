# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="del_test_contact", midname="del_test_contact_Mid", surname="del_test_contact_sur", nick="del_test_contact_nick", \
                                    title="del_test_contact_title", co="del_test_contact_co", addr="del_test_contact_addr", hometel="del_test_contact_tel",\
                                    mobtel="del_test_contact_mob", worktel="del_test_contact_work", fax="del_test_contact_fax", email="del_test_contact_e",\
                                    bday="del_test_contact_d", bmonth="del_test_contact_m", byear="del_test_contact_y", groupname="del_test_contact_group"))
    app.contact.delete_first()
