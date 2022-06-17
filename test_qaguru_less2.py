
from selene import be, have
from selene.core.condition import Condition
from selene.support.shared import browser

passed_search = 'selene'
failed_search = 'yashakaselenefpjsdfdjsolsdjjfoi'
passed_search_result = 'yashaka/selene: User-oriented Web UI browser tests in Python'


def test_to_find_selene_in_google(open_google):
    search(text=passed_search, condition=have.text(passed_search_result))


def test_failed_result_in_google(open_google):
    search(text=failed_search, condition=have.no.texts())


def search(text: str, condition: Condition):
    query = browser.element('[name="q"]')
    query.should(be.blank).type(text).press_enter()

    browser.element('#search').should(condition)