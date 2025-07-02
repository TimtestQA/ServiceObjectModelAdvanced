from faker import Faker

faker = Faker()

class Payloads:

    @staticmethod
    def add_item(item_uuid=None, quantity=None):
        return {
          "item_uuid": item_uuid or "1990ecdd-4d3d-4de2-91b9-d45d794c82bc",
          "quantity": quantity or 3
        }

    @staticmethod
    def add_item_with_invalid_quantity():
        return Payloads.add_item(quantity=-5)
