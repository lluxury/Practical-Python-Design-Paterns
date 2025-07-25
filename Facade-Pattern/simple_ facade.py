# simple_ facade.py
class Invoice:
    def __init__(self, customer):
        pass


class Customer:
    # Altered customer class to try to fetch a customer on init or creates a new one
    def __init__(self, customer_id):
        pass


class Item:
    # Altered item class to try to fetch an item on init or creates a new one
    def __init__(self, item_barcode):
        pass


class Facade:
    @staticmethod
    def make_invoice(customer):
        return Invoice(customer)

    @staticmethod
    def make_customer(customer_id):
        return Customer(customer_id)

    @staticmethod
    def make_item(item_barcode):
        return Item(item_barcode)