from app import calculate_total_value

def test_calculate_total_value():
    data = [{"price": 10, "quantity": 2}]
    assert calculate_total_value(data) == 20