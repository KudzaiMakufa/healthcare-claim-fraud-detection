from django import forms


class PasswordChangeForm(forms.Form):

    oldpass = forms.CharField(required=True , widget= forms.PasswordInput(
    attrs={
    
        "class":"form-control",
        "id":"oldpass",
    
        "placeholder":"Enter old password"
    }
    )) 

    newpass = forms.CharField(required=True , widget= forms.PasswordInput(
    attrs={
    
        "class":"form-control",
        "id":"newpass",

         "placeholder":"Enter new password"
    }
    )) 

    confirmpass = forms.CharField(required=True , widget= forms.PasswordInput(
    attrs={
    
        "class":"form-control",
        "id":"confirmpass",

         "placeholder":"Confirm password"
    }
    )) 