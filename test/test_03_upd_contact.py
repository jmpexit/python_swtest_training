# -*- coding: utf-8 -*-
from model.contact import Contact

def test_update_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(name="upd_test_contact", midname="upd_test_contact_Mid", surname="upd_test_contact_sur", nick="upd_test_contact_nick", \
                                    title="upd_test_contact_title", co="upd_test_contact_co", addr="upd_test_contact_addr", hometel="upd_test_contact_tel",\
                                    mobtel="upd_test_contact_mob", worktel="upd_test_contact_work", fax="upd_test_contact_fax", email="upd_test_contact_e",\
                                    bday="upd_test_contact_d", bmonth="upd_test_contact_m", byear="upd_test_contact_y", groupname="upd_test_contact_group"))
    app.contact.update_some(Contact(name="Uuu", midname="Mm", surname="Niiiiiii", nick="pinky", title="ti3", \
                                    co="very big co3", addr="USA, NY, B, sm.str, smth", hometel="111-11-13",\
                                    mobtel="1-111-111-1113", worktel="888-22-23", fax="888-22-23", email="uum@ex.ny",\
                                    bday="5", bmonth="January", byear="1986", groupname="group1"))