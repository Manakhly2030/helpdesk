# import frappe
from frappe import _
from frappe.contacts.doctype.contact.contact import Contact


class CustomContact(Contact):
    @staticmethod
    def default_list_data():
        columns = [
            {
                "label": "Name",
                "type": "Data",
                "key": "full_name",
                "width": "17rem",
            },
            {
                "label": "Email",
                "type": "Data",
                "key": "email_id",
                "width": "12rem",
            },
            {
                "label": "Phone",
                "type": "Data",
                "key": "phone",
                "width": "12rem",
            },
            {
                "label": "Last Modified",
                "type": "Datetime",
                "key": "modified",
                "width": "8rem",
            },
        ]
        rows = [
            "name",
            "full_name",
            "company_name",
            "email_id",
            "phone",
            "modified",
            "image",
        ]
        return {"columns": columns, "rows": rows}
