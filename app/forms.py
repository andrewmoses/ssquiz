from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextField, TextAreaField, SubmitField, validators, ValidationError, PasswordField, DateField, IntegerField, SelectField
from wtforms.validators import DataRequired
from app import db
from .models import User
import MySQLdb
import datetime

class LoginForm(Form):
    userid = StringField('userid', validators=[DataRequired()])
    password1 = PasswordField('password1', [validators.Length(min=6)])


class enterinForm(Form):

  password = PasswordField('Password', [validators.Required("Please_enter_the_password.")])
  submit = SubmitField("Sign In")

  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)

  def validate(self):
    if not Form.validate(self):
        return False
    i = datetime.datetime.now()
    strnum = str(i.day)
    lastdigit = strnum[len(strnum)-1]
    #password list
    pwd = ['chicken','mutton','beef','samosa','idly','dosa','rice','sambar','stone','paper']
    #today's password
    todaypwd = pwd[int(lastdigit)]
    if todaypwd==self.password.data:
        return True
    else:
        self.password.errors.append("Wrong_password")
        return False


class questionForm(Form):

    creator = TextField("creator", [validators.Required("Please_enter_your_name")])
    creator1 = TextField("creator1", [validators.Required("Example_Judges_19")])
    originalquestion = TextAreaField("originalquestion", [validators.Required("Please_enter_your_questions")])
    originalanswer = TextAreaField("originalanswer", [validators.Required("Please_enter_your_answers")])


    submit = SubmitField("create")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True



class answerForm(Form):

    creator = TextField("creator", [validators.Required("Please_enter_your_name")])
    originalquestion = TextAreaField("originalquestion", [validators.Required("Please_enter_your_answers")])

    submit = SubmitField("create")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        else:
            return True









class newjobForm(Form):
    job_title = TextField("job title", [validators.Required("Please_enter_the_Title_of_the_Job")])
    job_lastdate = DateField("Last Date", [validators.Required("eg.dd-mm-yyyy")], format = '%d-%m-%Y')
    job_vaccancies = IntegerField('vaccancies', [validators.Required("Enter_the_number_of_vaccancies") ])
    job_lookingfor = TextField("Looking for", [validators.Required("eg.Beginner")])
    job_ctc = TextField("Salary", [validators.Required("Please_enter_the_salary_package")])
    job_contract = TextField("job contract", [validators.Required("Select_yes_or_no")])
    job_workingdays = IntegerField("job workingdays", [validators.Required("Number_of_workingdays")])
    job_refer = TextField("reference for the job", [validators.Required("Select_yes_or_no")])
    job_desc = TextField("job description", [validators.Required("Describe_the_job")])
    job_skills = TextField("job skills", [validators.Required("Enter_the_skills")])
    job_company = TextField("job company", [validators.Required("Enter_the_company")])
    submit = SubmitField("create the job")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
	    return False

        else:
            return True
