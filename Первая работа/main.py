from data import db_session
from flask import Flask
from data.jobs import Jobs
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'rybolovlevalexey_secret_key'


def main():
    db_session.global_init('db/mars_explorer.db')

    ex_job = Jobs()
    ex_job.team_leader = 1
    ex_job.job = 'deployment of residential modules 1'
    ex_job.work_size = 15
    ex_job.collaborators = 2
    ex_job.start_date = datetime.date.today()
    ex_job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(ex_job)
    db_sess.commit()

    ex_job = Jobs()
    ex_job.team_leader = 1
    ex_job.job = 'deployment of residential modules 2'
    ex_job.work_size = 20
    ex_job.collaborators = 3
    ex_job.start_date = datetime.date.today()
    ex_job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(ex_job)
    db_sess.commit()
    #app.run()


if __name__ == '__main__':
    main()
