from django import forms
from django.contrib.auth.models import User
from .models import Assesment, Question, Answer, Result

from students.models import Student
from django.forms.models import modelformset_factory
from django.db.models import Count

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, Reset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.template.defaultfilters import default


class QuestionForm(forms.ModelForm):
    question_image = forms.ImageField(required=False)
    question_text = forms.CharField(label="Question ", widget=forms.Textarea(attrs={'rows':14, 'cols':50}))
    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        
        
        '''
        self.fields['question_image'].help_text = "File(jpg/jpeg/png) Size Should Be Less Than 500kb. "
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.form_id = 'action_question_add'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-8'
        self.helper.form_show_errors = True
        self.helper.form_error_title = "error of form"
        self.helper.formset_error_title ="E formset"
        self.helper.layout = Layout(
                                HTML("""
                                        <div class="container">
                                        <div class="col-md-12">
                                """),
                                    
                                Fieldset(
                                    'Please Use the below form for adding a Question to Assesment',
                                  
                                   'question_text',
                                   'question_image',
                                   'max_marks',
                                   
                                   
                                   Field('question_type',style="height: 34px;", title="What kind of question you want to create ?", css_class="select", css_id="which_question"),
                                   
                                   Field('brief_answer',style="", title="Please Enter Correct Answer For Reference", css_class="", css_id="reference_answer"),
                                   Div(
                                   Field('option_one',style="", title="Please Enter Option For Answer", css_class="", css_id="option_one"),
                                   Field('option_two',style="", title="Please Enter Option For Answer", css_class="", css_id="option_two"),
                                   Field('option_three',style="", title="Please Enter Option For Answer", css_class="", css_id="option_three"),
                                   Field('option_four',style="", title="Please Enter Option For Answer", css_class="", css_id="option_four"),
                                   Field('option_five',style="", title="Please Enter Option For Answer", css_class="", css_id="option_five"),
                                   
                                   Field('correct_options', type='hidden', style="", title="", css_class=""),
                                   HTML("""
                                        <p class="col-md-12">Please Choose The correct options</p>
                                        """),
                                   css_id = 'option-fields',
                                   css_class="form-group"
                                   ),
                                         
                                 
                                   
                                ),
                                 HTML("""
                                        <p class="col-md-12">Please click on submit, <strong>for creating the question</strong></p>
                                """),
                                
                                Div(
                                         Submit('submit', 'Submit', css_class='btn-primary '),
                                         Div(
                                             css_class="col-md-1"
                                             ),
                                         Reset('name', 'Reset', css_class='btn btn-danger'),
                                      css_class="col-md-12 row"),
                                HTML("""</div> </div>""")
                            )
        #self.helper.add_input()'''
        
    
    class Meta:
        model   = Question
        fields  = ('__all__')
        exclude = ['deleted_by','deleted_at', 'created_by', 'updated_by', 'assesment_linked']
    
    

    
    


class ReviewSqaAnswerForm(forms.ModelForm):
    written_answer = forms.CharField(label="Written Brief Answer: ", widget=forms.Textarea(attrs={'rows':14, 'cols':50}))
    def __init__(self, *args, **kwargs):
        super(ReviewSqaAnswerForm, self).__init__(*args, **kwargs)
        #self.fields['question_text']=forms.ModelChoiceField(queryset=Question.objects.filter(question_text="sdf"))
            
        
        
    class Meta:
        model   = Answer
        fields  = ['for_question','written_answer', 'alloted_marks']
        exclude = ['deleted_by','deleted_at', 'created_by', 'updated_by','opted_choice','for_result']
        widgets = {
          'written_answer': forms.Textarea(attrs={'rows':14, 'cols':50}),
        }


ReviewSqaFormSetBase = modelformset_factory(Answer,extra=0,form=ReviewSqaAnswerForm)

class ReviewSqaFormSet(ReviewSqaFormSetBase):
  
  def add_fields(self, form, index):
    super(ReviewSqaFormSet, self).add_fields(form, index)
    #form.fields['is_checked'] = forms.BooleanField(required=False)
    #form.fields['somefield'].widget.attrs['class'] = 'somefieldclass'

class ReviewSqaFormSetHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(ReviewSqaFormSetHelper, self).__init__(*args, **kwargs)
        
        self.form_method = 'post'
        self.form_action = '.'
        self.layout = Layout(
                                    Field('for_question',style="height: 34px;", title="Question text of the asked answer?", css_class="select", css_id="",readonly=True),
                                    Field('written_answer',style="height: 34px;", title="Question text of the asked answer?", css_class="select", css_id="", readonly=True),
                                    Field('alloted_marks',style="height: 34px;", title="Question text of the asked answer?", css_class="select", css_id=""),
                                    
                                    #FormActions(Submit('submit', 'Update Marks'))
            
                                )
        self.add_input(Submit("submit", "Update Marks"))
        self.render_required_fields = True
        
class CustomOptionsForAssesment(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
         return obj.get_student_name_for_staff()
        
        
class AssessmentForm(forms.ModelForm):
    DURATION_HOURS_CHOICES = [
        (i,i) for i in range(0,24)
        ]
    
    DURATION_MINUTES_CHOICES = [
        (i,i) for i in range(0,60)
        ]
    
    duration_hours = forms.ChoiceField(choices=DURATION_HOURS_CHOICES, required=True)
    duration_minutes = forms.ChoiceField(choices=DURATION_MINUTES_CHOICES, required=True)
    
    expired_on = forms.SplitDateTimeField(input_date_formats=['%Y-%m-%d'],
                               input_time_formats=['%H:%M:%S'], 
                               widget=forms.SplitDateTimeWidget(date_format='%Y-%m-%d',
                                                          time_format='%H:%M:%S',
                                                          attrs={'class':'form-control'}),
                                                          
                               )
                               
    exam_start_date_time = forms.SplitDateTimeField(input_date_formats=['%Y-%m-%d'],
                               input_time_formats=['%H:%M:%S'], 
                               widget=forms.SplitDateTimeWidget(date_format='%Y-%m-%d',
                                                          time_format='%H:%M:%S',
                                                          attrs={'class':'form-control'}),
                                                          
                               )
    
    
    subscriber_users = CustomOptionsForAssesment(queryset = Student.objects.filter(id=1),
                                                      widget=forms.CheckboxSelectMultiple())
    
    
    
    class Meta:
        model = Assesment
        
        fields = ('header', 'brief', 'exam_start_date_time', 'passing_marks', 'privilege', 'expired_on', 'subscriber_users')
        exclude= ['deleted_by','deleted_at', 'created_by', 'updated_by', 'exam_start_type', 'is_exam_active']
        labels = {
        "header": "Short Heading",
        "privilege": "Visibility",
        }
        widgets = {
            'header': forms.TextInput(
                                       attrs={'class':'form-control'}
                                    ),
            'brief': forms.Textarea(
                                       attrs={'class':'form-control'}
                                    ),
            
            'passing_marks'         : forms.NumberInput(attrs={'class':'form-control',}),
            'privilege'             : forms.Select(attrs={'class':'custom-select custom-select-md mb-3', 'data-toggle':"tooltip", 'data-placement':"right", 'title':"<h5>Public: Assesment Visibile to Students \n Private and Protected: Only To Staff</h3>"}),
            

        }
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AssessmentForm, self).__init__(*args, **kwargs)
        
        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        #self.helper = FormHelper(self)
        self.fields["subscriber_users"].queryset = Student.active.filter(staffuser__institute = self.request.user.staff.institute)   
         
class AssessmentCreationForm(forms.ModelForm):
    DURATION_HOURS_CHOICES = [
        (i,i) for i in range(0,24)
        ]
    
    DURATION_MINUTES_CHOICES = [
        (i,i) for i in range(0,60)
        ]
    
    duration_hours = forms.ChoiceField(choices=DURATION_HOURS_CHOICES, required=True)
    duration_minutes = forms.ChoiceField(choices=DURATION_MINUTES_CHOICES, required=True)
    
    expired_on = forms.SplitDateTimeField(input_date_formats=['%Y-%m-%d'],
                               input_time_formats=['%H:%M:%S'], 
                               widget=forms.SplitDateTimeWidget(date_format='%Y-%m-%d',
                                                          time_format='%H:%M:%S',
                                                          attrs={'class':'form-control'}),
                                                          
                               )
    exam_start_date_time = forms.SplitDateTimeField(input_date_formats=['%Y-%m-%d'],
                               input_time_formats=['%H:%M:%S'], 
                               widget=forms.SplitDateTimeWidget(date_format='%Y-%m-%d',
                                                          time_format='%H:%M:%S',
                                                          attrs={'class':'form-control'}),
                                                          
                               )

    subscriber_users = CustomOptionsForAssesment(queryset = Student.objects.filter(id=1),
                                                      widget=forms.CheckboxSelectMultiple())
    
    class Meta:
        model = Assesment
        fields = ('__all__')
        exclude= ['deleted_by','deleted_at', 'created_by', 'updated_by', 'exam_start_type','total_exam_duration', 'is_exam_active']
        
        labels = {
        "header": "Short Heading",
        "privilege": "Visibility",
        }
        widgets = {
            'header': forms.TextInput(
                                       attrs={'class':'form-control'}
                                    ),
            'brief': forms.Textarea(
                                       attrs={'class':'form-control'}
                                    ),
            
            'passing_marks'         : forms.NumberInput(attrs={'class':'form-control',}),
            'privilege'             : forms.Select(attrs={'class':'custom-select custom-select-md mb-3', 'data-toggle':"tooltip", 'data-placement':"right", 'title':"Public: Assessment Visible to Students. \n\n Private and Protected: Assessment Visible Only To Staff"}),
            
                   
            
        }    
       
    
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AssessmentCreationForm, self).__init__(*args, **kwargs)
        self.fields["subscriber_users"].queryset = Student.active.filter(staffuser__institute = self.request.user.staff.institute)    
    
    
    