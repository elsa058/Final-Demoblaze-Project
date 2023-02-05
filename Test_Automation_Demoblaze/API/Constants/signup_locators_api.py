from random import randint

class RegisterConstants:
    num = randint(1, 2500)
    url_register = 'https://api.demoblaze.com/signup'
    data_valid = {'name': "Elsa",
                  'password': "1234"}
    data_invalid_password = {'name': "elsades",
                             'password': "1234"}
    data_invalid_empty_user_name = {'name': " ",
                                    'password': "123"}
    data_invalid_empty_passwerd = {'name': "elsades@gamil.com",
                                   'password': ""}
    data_invalid_invalid_user_name = {'name': "elsa ",
                                    'password':"123567"}