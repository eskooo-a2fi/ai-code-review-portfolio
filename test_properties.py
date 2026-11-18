from corrected_fibonacci import fibonacci


def test_recurrence_holds_across_first_fifty_terms():
    for index in range(2, 51):
        assert fibonacci(index) == fibonacci(index - 1) + fibonacci(index - 2)


def test_large_result_can_be_computed_without_recursive_depth_limits():
    assert fibonacci(500) > 10 ** 100
