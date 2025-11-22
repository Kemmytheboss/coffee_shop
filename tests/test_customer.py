import pytest
from customer import Customer
from coffee import coffee

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("") 
    with pytest.raises(ValueError):
        Customer("A" * 51)
    c = Customer("John Doe")
    assert c.name == "John Doe"