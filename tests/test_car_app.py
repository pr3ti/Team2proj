import pytest
from carapp import cars

# Sample test for adding a car
def test_add_car():
    new_car = {"id": 3, "make": "Ford", "model": "Focus", "year": 2019}
    cars.append(new_car)
    
    assert new_car in cars  # Check if the new car is added
    assert len(cars) == 3   # Ensure the total count is correct

# Sample test for deleting a car
def test_delete_car():
    global cars
    initial_length = len(cars)
    
    cars = [car for car in cars if car["id"] != 1]  # Removing car with ID 1
    
    assert len(cars) == initial_length - 1  # Ensure one car is removed
    assert all(car["id"] != 1 for car in cars)  # Make sure ID 1 no longer exists

# Sample test for updating a car
def test_update_car():
    for car in cars:
        if car["id"] == 2:
            car["make"] = "Hyundai"
            car["model"] = "Elantra"
            car["year"] = 2022
            break

    updated_car = next((car for car in cars if car["id"] == 2), None)

    assert updated_car is not None
    assert updated_car["make"] == "Hyundai"
    assert updated_car["model"] == "Elantra"
    assert updated_car["year"] == 2022
