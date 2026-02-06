from checker import is_strong

def test_strong():
    assert is_strong("Abc!1234")

def test_weak():
    assert not is_strong("abc123")
