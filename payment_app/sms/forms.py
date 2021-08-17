from .models import *
from django import forms


class docform(forms.ModelForm):
    class Meta:
        model = documents
        fields = "__all__"

class cxform(forms.ModelForm):

    class Meta:
        model = customer
        fields = "__all__"  
        excluded = ("email",)    


class poiForm(forms.ModelForm):
    class Meta:
        model = documents
        fields = ["email","poi"]

class poaFrontForm(forms.ModelForm):
    class Meta:
        model = documents
        fields = ["email","poaFront"]

class poaBackForm(forms.ModelForm):
    class Meta:
        model = documents
        fields = ["email","poaBack"]

class livePicForm(forms.ModelForm):
    class Meta:
        model = documents
        fields = ["email","livePic"]

class nachMandateForm(forms.ModelForm):
    class Meta:
        model = documents
        fields = ["email","nachMandate"]

class loanAgreementForm(forms.ModelForm):
    class Meta:
        model = documents
        fields = ["email","loanAgreement"]

class bankProofForm(forms.ModelForm):
    class Meta:
        model = documents
        fields = ["email","bankProof"]

class statementsForm(forms.ModelForm):
    class Meta:
        model = statements
        exclude = ("loanStatus",)