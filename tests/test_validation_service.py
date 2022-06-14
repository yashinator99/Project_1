from flask import Flask
from service.validation_service import *
import pytest

# working impl
@pytest.mark.parametrize("test_name, expected", (
    ("B", False), (" ", False), ("..", False), ("Sm", False), ("Ti", False),
    ("adkjfkasjfkjfkasjfkjaskfdjkfjskfjsk", False),
    (".......................asf;ksal;fklaskflkflsklf", False),
    ("1313132",False), ("asdf adsfsa", False),
    ("Smith", True), ("Smith12", True), ("Tom1234", True), ("Thomas1234", False)
))
def test_validate_username(test_name, expected):
    assert validate_username(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
    ("B", False), (" ", False), ("..", False), ("Sm", False), ("Ti", False),
    ("adkjfkasjfkjfkasjfkjaskfdjkfjskfjsk", False),
    (".......................asf;ksal;fklaskflkflsklf", False),
    ("1313132",False), ("asdf adsfsa", False),
    ("Smith", False), ("Smiths1255", True), ("Tierny123", True), ("Thomas1234", True)
))
def test_validate_password(test_name, expected):
    assert validate_password(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
    ("B", False), (" ", False), ("..", False), ("Sm", False), ("Ti", False),
    ("adkjfkasjfkjfkasjfkjaskfdjkfjskfjsk", False),
    (".......................asf;ksal;fklaskflkflsklf", False),
    ("1313132",False), ("asdf adsfsa", False),
    ("Smith", False), ("manager", True), ("employee", True), ("pending", False)
))
def test_validate_role(test_name, expected):
    assert validate_role(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
     ("asonjdfkfsdouniorernfopqeurebhgikaberoisdfsdfsdfsdfsgdgkbeahrgijhabergjlhaebrgdfzjvnvdjfkbnvdzkjfgbdzlkfgbdzl", False), ("hello", True),
     ("",True), (".",True), ("This sentence will be exactly one hundred characters so that this may or may not pass the test cases", True)
))
def test_validate_description(test_name, expected):
    assert validate_request_desc(test_name) == expected


@pytest.mark.parametrize("test_name, expected", (
     ("25", True), (241, True), (1, True), (1000, True), ("1", True), ("1000", True),
     (-1,False), ("-1", False), (0, False), ("1001",False), (1001,False),
     ("asd",False), ("1e1", False), ("100e23", False), ("1001",False), ("12dsa3",False)
))
def test_validate_description(test_name, expected):
    assert validate_request_amount(test_name) == expected