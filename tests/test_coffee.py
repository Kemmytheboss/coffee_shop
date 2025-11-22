import pytest
from coffee import MENU

def test_customer_name_validation():
    with pytest.raises(ValueError):
        coffee("abc")  # Invalid name
    c = coffee("Latte")
    assert c.name == "Latte"