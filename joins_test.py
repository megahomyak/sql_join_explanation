from collections import Counter
from typing import NamedTuple, Optional

import joins
import table_samples


class CatNameToShopName(NamedTuple):
    cat_name: Optional[str]
    shop_name: Optional[str]


query_parameters = dict(
    left=table_samples.cats,
    right=table_samples.shops,
    condition=lambda cat, shop: cat.shop_id == shop.id,
    fields_filter=lambda cat, shop: CatNameToShopName(
        (cat and cat.name), (shop and shop.name)
    )
)


def test_joins():
    assert Counter(joins.full_join(
        left=[(1,), (1,)],
        right=[(1,), (2,)],
        condition=lambda left, right: left[0] == right[0],
        fields_filter=lambda left, right: (left and left[0], right and right[0])
    )) == {
        (1, 1): 2,
        (None, 2): 1
    }

    assert Counter(joins.inner_join(
        **query_parameters
    )) == {
        CatNameToShopName("Vlas", "Four Paws"): 1,
        CatNameToShopName("Nemo", "Mr.Zoo"): 1
    }

    assert Counter(joins.left_join(
        **query_parameters
    )) == {
        CatNameToShopName("Vlas", "Four Paws"): 1,
        CatNameToShopName("Nemo", "Mr.Zoo"): 1,
        CatNameToShopName("Vicont", None): 1,
        CatNameToShopName("Zuza", None): 1
    }

    assert Counter(joins.right_join(
        **query_parameters
    )) == {
        CatNameToShopName("Vlas", "Four Paws"): 1,
        CatNameToShopName("Nemo", "Mr.Zoo"): 1,
        CatNameToShopName(None, "Murzila"): 1,
        CatNameToShopName(None, "Cats&Dogs"): 1
    }

    assert Counter(joins.full_join(
        **query_parameters
    )) == {
        CatNameToShopName("Vlas", "Four Paws"): 1,
        CatNameToShopName("Nemo", "Mr.Zoo"): 1,
        CatNameToShopName("Vicont", None): 1,
        CatNameToShopName("Zuza", None): 1,
        CatNameToShopName(None, "Murzila"): 1,
        CatNameToShopName(None, "Cats&Dogs"): 1
    }
