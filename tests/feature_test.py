from my_minimal_project.feature import add


def test_add():
    """test add function"""
    assert add(1, 2) == 3
    assert add(2, 3) == 5
    assert add(3, 4) == 7
