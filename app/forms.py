from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, 

class ContactForm(Form):
    name = TextField("Name")
    desc = TextAreaField("Description")
    submit = SubmitField("Send")
