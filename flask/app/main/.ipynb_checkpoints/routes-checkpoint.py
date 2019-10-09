from flask import render_template
         
from app.main import bp  # noqa
from app.models.job import Job 
         
         
@bp.route('/')
def index():
    """Main page route."""
    button_text = "Add Job"
    return render_template('main.html', button_text=button_text)
         
         
@bp.route('/add_job')
def add_job():
    """Adds job4 to the database."""
    new_job = Job(name='job4')
    new_job.insert()                                                                                                                                                         
    return ('', 204) 
