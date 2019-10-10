from flask import render_template

from app_teste import bp
from app_teste.models.job import Job

@bp.route('/')
def index():
    button_text = "ADD JOB"
    return render_template('main.html', button_text=button_text)

@bp.route('/add_job')
def add_job():
    new_job = Job(name='job4')
    new_job.insert()
    return ('',204)
