from app import app, db
from app.models import Credentials,Studentdetails


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Credentials': Credentials,'Studentdetails':Studentdetails}
