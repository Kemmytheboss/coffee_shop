import pytest
from coffee import Coffee
from customer import Customer

def test_customer_name_validation():
    with pytest.raises(ValueError):
        coffee("abc")  # Invalid name
    c = coffee("Latte")
    assert c.name == "Latte"