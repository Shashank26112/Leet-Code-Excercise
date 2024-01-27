class Storage:
    def __init__(self, storage_type):
        self.storage_type = storage_type
        self.products = []

def receive_shipment(product_ids, temperature_threshold):
    cold_storage = Storage('cold')
    normal_storage = Storage('normal')

    for product_id in product_ids:
        temperature = product_ids[product_id]['temperature']
        if temperature < temperature_threshold:
            cold_storage.products.append(product_id)
        else:
            normal_storage.products.append(product_id)

    print_storage_lists(cold_storage, normal_storage)

def print_storage_lists(cold_storage, normal_storage):
    print("Products in cold storage:")
    print(cold_storage.products)
    print("\nProducts in normal storage:")
    print(normal_storage.products)

# Example usage:
product_ids = [1, 2, 3, 4, 5]
product_ids = {1: {'temperature': 5}, 2: {'temperature': 10}, 3: {'temperature': 15}, 4: {'temperature': 20}, 5: {'temperature': 25}}

receive_shipment(product_ids, 10)