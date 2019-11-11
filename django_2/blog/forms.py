from django.forms import Form, CharField, EmailField, Textarea

class EmailPostForm(Form):
    name = CharField(max_length=25)
    email = EmailField()
    to = EmailField()
    comments = CharField(required=False,
                         widget=Textarea)