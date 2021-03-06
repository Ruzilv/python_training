import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_proverka(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="dfred", header="rtyhgvbn", footer="cvfgtrrr"))
    app.session.logout()


def test_empty_proverka(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
