from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError, BooleanField

class JobForm(Form):
    name = TextField("Name", [validators.Required("Please Enter Your Name")])
    desc = TextAreaField("Description",
            [validators.Required("Please Give a Description of the Problem")])
    submit = SubmitField("Send")
    delete = SubmitField("Delete")
