from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from dashboard.models import Library 

# model form 
from django.db import models
# from django.forms import ModelForm , Textarea , ModelChoiceField , Select  
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class Library_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'form-horizontal mr-auto ml-auto'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'

        self.helper.add_input(Submit('submit', 'Submit Claim for Processing'))
        
    class Meta:
        model = Library
        
        
        fields = ['provider_id','physician_id','operating_physician','other_physician','patient_id','gender' ,'race','state',
                    'country','RenalDiseaseIndicator','Alzheimer','Heartfailure','KidneyDisease','Cancer','ObstrPulmonary','Depression',
                    'Diabetes','IschemicHeart','Osteoporasis','Arthritis','Stroke','diagnosis_1','diagnosis_2','diagnosis_3','diagnosis_4',
                    'diagnosis_5','diagnosis_6','diagnosis_7','diagnosis_8','diagnosis_9','diagnosis_10','procedure_1','procedure_2','procedure_3',
                    'procedure_4','procedure_5','procedure_6','DiagnosisGroupCode','ClmAdmitDiagnosisCode','no_of_days_admitted','no_of_days_for_claim',
                    'total_insurance_reimbursed','total_deductable_paid','amount_reimbursed_as_inpatient','amount_reimbursed_as_outpatient',
                    'total_deductable_paid_as_outpatient' 
                ]

             
   

