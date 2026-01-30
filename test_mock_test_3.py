import pytest
import inspect
import practice  


def test_taxi_fare_calculator():
    # Case 1: Simple single trips
    trips = [("Thabo", 5), ("Nandi", 10)]
    # Thabo: 15 + (2 * 5) = 25
    # Nandi: 15 + (2 * 10) = 35
    expected = {"Thabo": 25, "Nandi": 35}
    assert practice.taxi_fare_calculator(trips) == expected

    # Case 2: Accumulating trips for same person
    trips_mixed = [("Thabo", 5), ("Nandi", 10), ("Thabo", 2)]
    # Thabo Trip 1: 25
    # Thabo Trip 2: 15 + (2 * 2) = 19. Total = 44
    expected_mixed = {"Thabo": 44, "Nandi": 35}
    assert practice.taxi_fare_calculator(trips_mixed) == expected_mixed

    # Case 3: Empty input
    assert practice.taxi_fare_calculator([]) == {}


def test_format_id_numbers():
    input_ids = ["900101-5000-087", " 850505 5000 081 ", "920202.5000.082"]
    expected = [
        "ID: 9001015000087",
        "ID: 8505055000081",
        "ID: 9202025000082"
    ]
    assert practice.format_id_numbers(input_ids) == expected

    # Edge case: Empty list
    assert practice.format_id_numbers([]) == []


def test_recursive_countdown():
    # Check functionality
    assert practice.recursive_countdown(3) == "3...2...1...0...Happy New Year!"
    assert practice.recursive_countdown(0) == "0...Happy New Year!"
    
    # CHECK RECURSION: Ensure the function calls itself
    source = inspect.getsource(practice.recursive_countdown)
    # This checks if the function name appears inside its own body
    assert "recursive_countdown(" in source, "Error: You must use recursion, not a loop."


def test_unique_ingredients():
    recipes = [
        ["Onions", "Tomatoes", "Ginger"], 
        ["Garlic", "Onions", "Chili"], 
        ["Tomatoes", "Coriander"]
    ]
    # Should be sorted and unique
    expected = ['Chili', 'Coriander', 'Garlic', 'Ginger', 'Onions', 'Tomatoes']
    assert practice.unique_ingredients(recipes) == expected
    
    # Check return type is a list (even though logic uses Set)
    assert isinstance(practice.unique_ingredients(recipes), list)


def test_student_average():
    gradebook = {
        "Lerato": [50, 60, 70],      # Avg 60.0
        "Limpho": [80, 85, 90],     # Avg 85.0
        "Sipho": [55, 65, 55, 65]    # Avg 60.0
    }
    expected = {
        "Lerato": 60.0,
        "Limpho": 85.0,
        "Sipho": 60.0
    }
    assert practice.student_average(gradebook) == expected

    # Check rounding
    # 100 / 3 = 33.3333... should be 33.33
    assert practice.student_average({"Test": [100, 0, 0]}) == {"Test": 33.33}


def test_recursive_string_reverse():
    # Functionality
    assert practice.recursive_string_reverse("Python") == "nohtyP"
    assert practice.recursive_string_reverse("racecar") == "racecar"
    assert practice.recursive_string_reverse("") == ""

    # CHECK RECURSION
    source = inspect.getsource(practice.recursive_string_reverse)
    assert "recursive_string_reverse(" in source, "Error: You must use recursion."
    # Ban specific shortcuts
    assert "[::-1]" not in source, "Error: Do not use slicing [::-1]"
    assert "reversed(" not in source, "Error: Do not use reversed()"


def test_whatsapp_parser():
    log_data = [
        "[14:00] Admin: Meeting starts now",
        "[14:05] User1: Hello everyone"
    ]
    expected = [
        {'time': '14:00', 'user': 'Admin', 'message': 'Meeting starts now'},
        {'time': '14:05', 'user': 'User1', 'message': 'Hello everyone'}
    ]
    assert practice.whatsapp_parser(log_data) == expected
    
    # Ensure keys are correct
    result = practice.whatsapp_parser(log_data[:1])
    assert "time" in result[0]
    assert "user" in result[0]
    assert "message" in result[0]


def test_find_missing_items():
    stock = ("Coke", "Chips", "Bread", "Milk")
    sold = {"Coke", "Bread"}
    
    # Result should be a Set
    result = practice.find_missing_items(stock, sold)
    assert isinstance(result, set)
    assert result == {"Chips", "Milk"}
    
    # Case where nothing is missing
    assert practice.find_missing_items(("A", "B"), {"A", "B"}) == set()


def test_recursive_fibonacci():
    # Seq: 0, 1, 1, 2, 3, 5, 8
    assert practice.recursive_fibonacci(0) == 0
    assert practice.recursive_fibonacci(1) == 1
    assert practice.recursive_fibonacci(6) == 8
    
    # CHECK RECURSION
    source = inspect.getsource(practice.recursive_fibonacci)
    assert "recursive_fibonacci(" in source, "Error: You must use recursion."


def test_invoice_formatter():
    items = {"Bread": 15.5, "Milk": 22}
    output = practice.invoice_formatter(items)
    
    # Split into lines to check specific formatting
    lines = output.strip().split('\n')
    assert len(lines) == 2
    
    # Check Bread line
    bread_line = lines[0]
    assert "Bread" in bread_line
    assert "R 15.50" in bread_line
    # Check total length is 30
    assert len(bread_line) == 30
    # Check that it ends correctly
    assert bread_line.endswith("R 15.50")
    
    # Check Milk line
    milk_line = lines[1]
    assert "R 22.00" in milk_line  # Checks for correct .2f formatting
    assert len(milk_line) == 30


def test_community_donations():
    donations = [
        {"Blankets": 5, "Water": 10},
        {"Blankets": 2, "Food": 20},
        {"Water": 5}
    ]
    expected = {"Blankets": 7, "Water": 15, "Food": 20}
    assert practice.community_donations(donations) == expected
    
    # Test empty
    assert practice.community_donations([]) == {}


def test_unpack_delivery():
    # Shallow nest
    assert practice.unpack_delivery(["A", ["B", "C"]]) == ["A", "B", "C"]
    
    # Deep nest
    nested = ["Shirt", ["Shoes", "Socks"], [["Cap"], "Belt"]]
    expected = ["Shirt", "Shoes", "Socks", "Cap", "Belt"]
    assert practice.unpack_delivery(nested) == expected
    
    # Empty
    assert practice.unpack_delivery([]) == []


def test_palindrome_detector():
    # Simple true
    assert practice.palindrome_detector("racecar") is True
    # Simple false
    assert practice.palindrome_detector("python") is False
    # Case and space ignored
    assert practice.palindrome_detector("Race Car") is True
    assert practice.palindrome_detector("Never odd or even") is True


def test_load_shedding_stats():
    # "001110011000" -> Total 5 ones. Streak 3.
    schedule = "001110011000"
    expected = {"total_hours_off": 5, "longest_streak": 3}
    assert practice.load_shedding_stats(schedule) == expected
    
    # No load shedding
    assert practice.load_shedding_stats("0000") == {"total_hours_off": 0, "longest_streak": 0}
    
    # Full blackout
    assert practice.load_shedding_stats("1111") == {"total_hours_off": 4, "longest_streak": 4}


def test_validate_rsa_id():
    # Valid
    assert practice.validate_rsa_id("9202205000087") is True
    
    # Invalid Length
    assert practice.validate_rsa_id("123") is False
    
    # Invalid Month (13)
    assert practice.validate_rsa_id("9913015000087") is False
    
    # Invalid Day (35)
    assert practice.validate_rsa_id("9901355000087") is False
    
    # Non-digits
    assert practice.validate_rsa_id("9901015000abc") is False