from django import forms
from .models import CustomerUser

class UserFormRigester(forms.Form):
    def __init__(self, *args, **kwargs):
            super(UserFormRigester, self).__init__(*args, **kwargs)
            for item in UserFormRigester.visible_fields(self):
                item.field.widget.attrs["class"] = "form-control "
    fullnameform = forms.CharField(max_length=100,label="نام و نام خانوادگی")
    usernameform = forms.CharField(max_length=100,label="نام کاربری")
    passwordform = forms.CharField(widget=forms.PasswordInput, label="رمز")
    id=forms.CharField(required=True,label="",widget=forms.HiddenInput(),initial="0")

class CheckForm(forms.Form):
    def __init__(self, *args, **kwargs):
            super(CheckForm, self).__init__(*args, **kwargs)
            for item in CheckForm.visible_fields(self):
                item.field.widget.attrs["class"] = "form-control "
    usernamecheck=forms.CharField(required=True,max_length=300,label="نام کابری")
    passwordcheck=forms.CharField(required=True,widget=forms.PasswordInput,label="رمز")

class FormEdit(forms.Form):
    def __init__(self, *args, **kwargs):
            super(FormEdit, self).__init__(*args, **kwargs)
            for item in FormEdit.visible_fields(self):
                item.field.widget.attrs["class"] = "form-control"
    Fullname = forms.CharField(required=True,max_length=100,label="نام و نام خانوادگی", label_suffix='')
    Username = forms.CharField(required=True,max_length=100, label="نام کاربری", label_suffix='')
    #pasword = forms.CharField(widget=forms.PasswordInput, label="رمز")
    id = forms.CharField(required=True, label="", widget=forms.HiddenInput(), initial="0")

class EditFormSendcustomermessage(forms.Form):
    def __init__(self, *args, **kwargs):
            super(EditFormSendcustomermessage, self).__init__(*args, **kwargs)
            for item in EditFormSendcustomermessage.visible_fields(self):
                item.field.widget.attrs["class"] = "form-control"
    fullname = forms.CharField(max_length=100, label="نام و نام خانوادگی")
    email = forms.EmailField(max_length=200, label="ایمیل")
    issue = forms.CharField(max_length=200, label="موضوع")
    message = forms.CharField(max_length=1000, label="پیام", widget=forms.Textarea())
    id = forms.CharField(label="", widget=forms.HiddenInput(), initial="0")

class FormSendcustomermessage(forms.Form):
    def __init__(self, *args, **kwargs):
            super(FormSendcustomermessage, self).__init__(*args, **kwargs)
            for item in FormSendcustomermessage.visible_fields(self):
                item.field.widget.attrs["class"] = "form-control "
    fulname=forms.CharField(max_length=100, label="نام و نام خانوادگی")
    email=forms.EmailField(max_length=200, label="ایمیل")
    issue=forms.CharField(max_length=200,label="موضوع")
    message=forms.CharField(max_length=1000,label="پیام",widget=forms.Textarea())
    id=forms.CharField(label="",widget=forms.HiddenInput(),initial="0")







'''
    Username = forms.CharField(required=True, label="نام کاربری", widget=forms.TextInput())
    Password = forms.CharField(required=True, label="رمز",widget=forms.PasswordInput())'''

'''class Meta:
        model = User
        fields = "__all__"'''
'''
class UserForm(forms.Form):
    username=forms.CharField(required=True,label="نام کاربری کامل")
    password=forms.CharField(required=True,label="رمزعبور", widget=forms.PasswordInput)

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = '__all__'
'''