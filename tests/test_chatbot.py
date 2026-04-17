from main import ChatbotApp

def test_phone_valid():
    app = ChatbotApp(None)
    assert app.validate_phone("0612345678") == True

def test_phone_invalid():
    app = ChatbotApp(None)
    assert app.validate_phone("12345") == False

def test_cin_valid():
    app = ChatbotApp(None)
    assert app.validate_cin("AB123456") == True

def test_cin_invalid():
    app = ChatbotApp(None)
    assert app.validate_cin("123") == False
