import sys

def get_size(obj, seen=None):
    """
    Recursively finds the size of an object in bytes.
    """
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum(get_size(key, seen) + get_size(value, seen) for key, value in obj.items())
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum(get_size(item, seen) for item in obj)
    return size

# Example usage:
my_list = [1, 2, 3, [4, 5], {'a': 6, 'b': [7, 8]}, "hello"]
size_of_my_list = get_size(my_list)
print(f"Size of my_list: {size_of_my_list} bytes")
