from typing import NamedTuple, Optional


class Cat(NamedTuple):
    name: Optional[str]
    shop_id: Optional[int]


class Shop(NamedTuple):
    id: Optional[int]
    name: Optional[str]


cats = [
    Cat(name="Vlas", shop_id=1),
    Cat("Nemo", 2),
    Cat("Vicont", 10),
    Cat("Zuza", None)
]


shops = [
    Shop(id=1, name="Four Paws"),
    Shop(2, "Mr.Zoo"),
    Shop(3, "Murzila"),
    Shop(4, "Cats&Dogs")
]
