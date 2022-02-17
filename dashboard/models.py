from django.db import models
from medclaim.settings import MEDIA_ROOT
class Provider(models.Model):

    provider_id  = models.CharField(default=None ,max_length=100)
    potential_fraud = models.CharField(default=None ,max_length=100)

    def __str__(self):
        return '%s' % self.provider_id+" potential fraud :"+self.potential_fraud

class Beneficiary(models.Model):

    beneficiary_id  = models.CharField(default=None ,max_length=100)
  

    def __str__(self):
        return '%s' % self.beneficiary_id+" Hidden Name & Surname"

class Physician(models.Model):

    physician_id  = models.CharField(default=None ,max_length=100)
  

    def __str__(self):
        return '%s' % self.physician_id

class Library(models.Model):
    
    GENDER = (('', '------'), ('0', 'Male'),('1', 'Female'),)
    # provider details
    provider_id = models.ForeignKey(Provider,on_delete=models.CASCADE , default=None)
   
    # physician details
    physician_id = models.ForeignKey(Physician,on_delete=models.CASCADE , default=None)
    operating_physician = models.ForeignKey(Physician,related_name='operating_physician' , on_delete=models.CASCADE , default=None)
    
    other_physician = models.ForeignKey(Physician,related_name='other_physician' , on_delete=models.CASCADE , default=None)
    # patient details
    patient_id = models.ForeignKey(Beneficiary,on_delete=models.CASCADE , default=None)
    gender = models.CharField(blank=True ,null=True, default='no' ,max_length=100 , choices = GENDER)
    race = models.CharField(default=None ,max_length=100)
    state = models.CharField(default=None ,max_length=100)
    country = models.CharField(default=None ,max_length=100)
    RenalDiseaseIndicator = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    Alzheimer  = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    Heartfailure  = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    KidneyDisease  = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    Cancer = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    ObstrPulmonary = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    Depression  = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    Diabetes  = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    IschemicHeart  = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    Osteoporasis  = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    Arthritis  = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    Stroke  = models.CharField(default=None,max_length=100 , choices = (('', '------'), ('1', 'Yes'),('0', 'No'),))
    # Treatment details
    diagnosis_1 = models.CharField(default=0 ,max_length=100)
    diagnosis_2 = models.CharField(default=0 ,max_length=100)
    diagnosis_3 = models.CharField(default=0 ,max_length=100)
    diagnosis_4 = models.CharField(default=0 ,max_length=100)
    diagnosis_5 = models.CharField(default=0 ,max_length=100)
    diagnosis_6 = models.CharField(default=0 ,max_length=100)
    diagnosis_7 = models.CharField(default=0 ,max_length=100)
    diagnosis_8 = models.CharField(default=0 ,max_length=100)
    diagnosis_9 = models.CharField(default=0 ,max_length=100)
    diagnosis_10 = models.CharField(default=0 ,max_length=100)

    # procedure details
    procedure_1 = models.CharField(default=0 ,max_length=100)
    procedure_2 = models.CharField(default=0 ,max_length=100)
    procedure_3 = models.CharField(default=0 ,max_length=100)
    procedure_4 = models.CharField(default=0 ,max_length=100)
    procedure_5 = models.CharField(default=0 ,max_length=100)
    procedure_6 = models.CharField(default=0 ,max_length=100)

    # other group codes details
    DiagnosisGroupCode  = models.CharField(default=0 ,max_length=100)
    ClmAdmitDiagnosisCode   = models.CharField(default=0 ,max_length=100)

    no_of_days_admitted = models.IntegerField(default=None)
    no_of_days_for_claim = models.IntegerField(default=None)

    # insurance amounts reimbursed by patient
    total_insurance_reimbursed = models.IntegerField(default=None)
    total_deductable_paid = models.IntegerField(default=None)
    amount_reimbursed_as_inpatient = models.IntegerField(default=None)
    amount_reimbursed_as_outpatient = models.IntegerField(default=None)
    total_deductable_paid_as_outpatient = models.IntegerField(default=None)
    is_fraudulent = models.BooleanField(default=False)
    updated_at = models.DateField(default=None)
    created_by = models.IntegerField(default=None)

    

    def __str__(self):
        return '%s' % self.application_name

