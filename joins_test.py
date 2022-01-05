import joins
import table_samples


query_parameters = {
    "left": table_samples.cats, "right": table_samples.shops,
    "condition": lambda cat, shop: cat.shop_id == shop.id,
    "fields_filter": lambda cat, shop: (
        (cat and cat.name), (shop and shop.name)
    )
}


def test_joins():
    assert joins.inner_join(
        **query_parameters
    ) == {
        # cat.name, shop.name
        ("Vlas", "Four Paws"),
        ("Nemo", "Mr.Zoo")
    }

    assert joins.left_join(
        **query_parameters
    ) == {
        # cat.name, shop.name
        ("Vlas", "Four Paws"),
        ("Nemo", "Mr.Zoo"),
        ("Vicont", None),
        ("Zuza", None)
    }

    assert joins.right_join(
        **query_parameters
    ) == {
        # cat.name, shop.name
        ("Vlas", "Four Paws"),
        ("Nemo", "Mr.Zoo"),
        (None, "Murzila"),
        (None, "Cats&Dogs")
    }

    assert joins.full_join(
        **query_parameters
    ) == {
        # cat.name, shop.name
        ("Vlas", "Four Paws"),
        ("Nemo", "Mr.Zoo"),
        ("Vicont", None),
        ("Zuza", None),
        (None, "Murzila"),
        (None, "Cats&Dogs")
    }
