import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_proverka(app):
    app.login(username="admin", password="secret")
    app.fill_group_form(Group(name="dfred", header="rtyhgvbn", footer="cvfgtrrr"))
    app.logout()


def test_empty_proverka(app):
    app.login(username="admin", password="secret")
    app.fill_group_form(Group(name="", header="", footer=""))
    app.logout()
