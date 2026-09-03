def sum(my_collection):
    total = 0
    for n in my_collection:
        total+= n
    return total

def test_sum_empty_list():
    assert sum([]) == 0

def test_sum_single_list():
    assert sum([1]) == 1

def test_sum_many_list():
    assert sum([4, 5, 8, 3, 9, 13]) == 42

def sum_tests():
    test_sum_empty_list()
    test_sum_single_list()
    test_sum_many_list()
    print("All sum tests passing.")