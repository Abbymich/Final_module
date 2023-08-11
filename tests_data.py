from faker import Faker

class Invalid_Data:
    fake_email = Faker().email()
    fake_password = Faker().password()
    fake_name = Faker().name()
    fake_last_name = Faker().last_name()
    first_name_1_char = 'Я'
    first_name_36_char = 'Екатеринаекатеринаекатеринаекатерина'
    last_name_1_char = 'Е'
    last_name_31_char = 'Екатеринаекатеринаекатеринаекат'
    password_22_char = 'Tests123456Tests123456'
    password_7_char = 'Tests12'
    password_no_Lower = 'Tests123455'
    password_not_contain_digit = "Tests1234560"
    xss = '<script>alert(123)</script>'
    email_without_domain = 'Test.QA@ru'
    invalid_phoneNumber = '+7922200000'

class Valid_Data:
    valid_first_name = 'Ян'
    valid_last_name = 'Пин-Че'
    valid_password = 'Tests123456'
    valid_phoneNumber = '+79222270220'
    valid_email = 'Tests.QA@yandex.ru'