 from flask import Flask
 from app_teste.database import DB
 from app_teste.models.job import Job
 
 
 def create_app(config):
     app = Flask(__name__)
     DB.init()
     register_blueprints(app)
     
     for job_name in ['job1', 'job2', 'job3']:
         new_job = Job(name=job_name)
         new_job.insert()
     
     return app

def register_blueprints(app):
    from app_teste.main import bp as main_bp
    app.register_blueprints(main_bp)
    
    
    
    
    
