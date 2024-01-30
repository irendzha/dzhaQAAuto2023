from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.nova_post_find_dep_page import FindDepPage
from modules.ui.page_objects.makeup_main_page import MakeupMainPage
from modules.ui.page_objects.ukrpost_sort_high_to_low import UkrPostMainPage
import pytest
import time

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    # створення обʼєкту сторінки
    sign_in_page = SignInPage()

    # відкриваємо сторінку https://github.com/login
    sign_in_page.go_to()

    # виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # закриваємо браузер 
    sign_in_page.close()

@pytest.mark.ui
def test_check_incorrect_department_page_object():
    # створення обʼєкту сторінки
    dep_page = FindDepPage()

    # відкриваємо сторінку https://novapost.com/uk-ua/departments?city=118064
    dep_page.go_to()
    time.sleep(10)

    # закриваємо опитувальник
    dep_page.click_survey()
    time.sleep(5)

    # вводимо неправильний номер відділення
    dep_page.try_search("99999")
    time.sleep(3)

    dep_page.check_title()

    dep_page.close()


@pytest.mark.ui
def test_redirect_to_youtube():
    # створення обʼєкту сторінки
    makeup_page = MakeupMainPage()

    # відкриваємо сторінку 'https://makeup.com.ua/ua/'
    makeup_page.go_to()

    # переходимо на канал makeup на ютубі
    makeup_page.go_to_makeup_youtube()

    # перевіряємо, що ми дійсно знаходимось на каналі makeup на ютубі
    assert makeup_page.check_url("https://www.youtube.com/user/makeupcomua/")

    makeup_page.close_brwsr()

@pytest.mark.ui
def test_add_to_cart():
    # створення обʼєкту сторінки
    ukrpost_page = UkrPostMainPage()

    # відкриваємо сторінку https://postmark.ukrposhta.ua/
    ukrpost_page.go_to()

    # обираємо категорію "Художні марки"
    ukrpost_page.search_merch()

    # сортуємо товари від найдорожчого до найдешевшого
    ukrpost_page.sort_high_to_low()

    # перевіряємо, що сортування застосувалось і ми знаходимось на правильній сторінці
    assert ukrpost_page.check_url("https://postmark.ukrposhta.ua/index.php?route=product/category&path=83_85&sort=p.price&order=DESC")
    time.sleep(3)

    ukrpost_page.close()
