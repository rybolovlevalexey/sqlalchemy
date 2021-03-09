from data import db_session
from flask import Flask
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'rybolovlevalexey_secret_key'


def main():
    db_session.global_init('db/mars_explorer.db')

    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Trump'
    user.name = 'Donald'
    user.age = 60
    user.position = 'matros'
    user.speciality = 'engineer'
    user.address = 'module_2'
    user.email = 'make_amerika_great_again@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = 'Putin'
    user.name = 'Vladimir'
    user.age = 70
    user.position = 'captain of the captain'
    user.speciality = 'economist'
    user.address = 'module_3'
    user.email = 'volodya777@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    #app.run()


if __name__ == '__main__':
    main()
