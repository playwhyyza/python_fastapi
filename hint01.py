from typing import List, Set, Tuple, Dict

def get_full_name(first_name: str, last_name: str):
    # then a dot (.) and then hint Ctrl + Space to trigger the completion
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name

def get_name_with_age(name: str, age: int):
    get_name_age = f"{name} is this old: {age}"
    return name_with_age

def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

def process_items(items: List[str]):
    """
        That means: 'the variable items is a list, and each of the items in this list is a str'.
        By doing that, your editor can provide support even while processing items from the list.
        Without types, that's almost impossible to achieve:

        Notice that the variable item is one of the elements in the list items.
        And still, the editor knows it is a str, and provides support for that.
    """
    for item in items:
        print(item)

def process_items2(items_t: Tuple[int], items_s: Set[bytes]):
    """
        The variable items_t is a tuple, and each of its items is an int.
        The variable items_s is a set, and each of its items is of type bytes.
    """
    return items_t, items_s

def process_items3(prices: Dict[str: float]):
    """
        The keys of this dict are of type str (let's say, the name of each item).
        The values of this dict are of type float (let's say, the price of each item)
    """
    for item_name, item_price in prices.items():
        print(f"{item_name}\n{item_price}")

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

if __name__ == "__main__":
    print(get_full_name("john", "doe"))
