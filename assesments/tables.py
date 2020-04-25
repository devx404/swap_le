import django_tables2 as tables
import itertools
from django.utils.html import format_html
from .models import Assesment, Question, Result
from django_tables2 import A

from django.urls import reverse

class ResultTable(tables.Table):
    
    
    #review_sqa = tables.LinkColumn('reviewsqa', text='Review Descriptive Answer')
    review_sqa = tables.TemplateColumn('<a href="{% url "staff:assesments:assesment_manage_review_sqa_question"  assesmentid=self.request.GET.assesmentid %}"><span class="fas fa-comments"></span></a>', verbose_name="Validate Descriptive Answer")
    result = tables.TemplateColumn('<a href="{% url "staff:assesments:assessment_result_by_staff" pk=record.pk %}"><center><span class="fas fa-file"></span></center></a>')
    exam_taken_date_time = tables.DateTimeColumn(accessor='exam_taken_date_time', verbose_name='Taken At')
    total_question = tables.Column(accessor='total_question', verbose_name='Questions')
    total_attempted = tables.Column(accessor='total_attempted', verbose_name='Attempted')
    total_marks = tables.Column(accessor='total_marks', verbose_name='Total')
    obtained_marks = tables.Column(accessor='obtained_marks', verbose_name='Obtained')
    result_passed = tables.BooleanColumn(accessor='result_passed', verbose_name='Passed')
    assesment_submitted = tables.BooleanColumn(accessor='assesment_submitted', verbose_name='Submitted')
    publish_result = tables.BooleanColumn(accessor='publish_result', verbose_name='Published')
    registered_user = tables.Column(accessor='registered_user', verbose_name='Student')
    
    def render_review_sqa(self, record):
        url = reverse('staff:assesments:assesment_manage_review_sqa_question',kwargs={'assesmentid': self.assesmentid})
        return format_html('<a href="{}"><span class="fas fa-comments">Validate Score</span></a>', url)
        
    def render_registered_user(self, record):
        reg_user = record.registered_user.get_name_registered_student()
        return format_html('{}'.format(reg_user))
    
    def __init__(self, *args, **kwargs):
        super(ResultTable, self).__init__(*args)
        self.counter = itertools.count()
        self.assesmentid = kwargs.get('assesmentid',None)
    
    
    
    class Meta:
        model = Result
        attrs = {'class': 'paleblue'}
        exclude = ('id', 'deleted_at','deleted_by','created_by','updated_by','type','assesment','created','updated',)

class QuestionTable(tables.Table):
    
    action = tables.TemplateColumn(' <div class="row"> <div class="col-md-6"> <a href=" {% url "staff:assesments:assessment_question_delete" assesmentid=record.assesment_linked.pk questionid=record.pk  %} "><center><span class="fas fa-trash-alt"></span></center></a></div></div>')
    
    def __init__(self, *args, **kwargs):
        super(QuestionTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()
    
    
        
    def render_question_text(self,value):
        return (value[:75] + '..') if len(value) > 75 else value
    class Meta:
        model = Question
        attrs = {'class': 'paleblue'}
        
        exclude = ('id', 'deleted_at','deleted_by','created_by','updated_by','created','updated', 'assesment_linked', 'question_image', 'option_one', 'option_two', 'option_three', 'option_four', 'option_five', 'correct_options', 'brief_answer' )

class AssesmentTable(tables.Table):
    edit =tables.TemplateColumn('<div class="col-md-12"><a alt="edit" class="btn-link"  href="{% url "staff:assesments:assessment_edit_by_staff"  assesmentid=record.id  %} "><center><span class="fas fa-edit "></span></center></a> </div>', orderable=False)
    delete = tables.TemplateColumn('<div class="col-md-12"> <a href=" {% url "staff:assesments:assessment_delete_by_staff" assesmentid=record.id  %} "><center><span class="fas fa-trash-alt"></span></center></a></div>', orderable=False)
    manage = tables.TemplateColumn('<div class="col-md-12"><a href=" {% url "staff:assesments:assessment_manage_by_staff" assesmentid=record.id  %} "><span class="fas fa-cogs "></span></a></div>',orderable=False)
    
    
    #manage_assesment = tables.TemplateColumn('<form method="GET"  action="{%  url "staff:assesments:assessment_manage_by_staff" %}">  {% csrf_token %} <input type="hidden" name="examid" value={{record.id }}> <input class="btn btn-dark" type="submit" value="Manage"> </form>')
    expired_on = tables.DateTimeColumn(accessor='expired_on', verbose_name='Expires On')
    exam_start_date_time = tables.DateTimeColumn(accessor='exam_start_date_time', verbose_name='Available From')
    def __init__(self, *args, **kwargs):
        super(AssesmentTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    

    def render_brief(self,value):
        return (value[:75] + '..') if len(value) > 75 else value
   
    class Meta:
        model = Assesment
        sequence = ( 'header','brief','exam_start_date_time', 'expired_on', 'passing_marks','privilege')
        # add class="paleblue" to <table> tag 
        attrs = {'class': 'paleblue'}
        # fields = ( 'institute',)
        exclude = ('id', 'brief', 'deleted_at','deleted_by','created', 'updated', 'created_by','updated_by','type','exam_start_type', 'is_exam_active')



class StudentAssesmentTable(tables.Table):
    
    
    take_assesment = tables.TemplateColumn('<form method="POST"  action=".">  {% csrf_token %} <input type="hidden" name="examid" value={{record.id }}> <input type="submit" class="btn btn-dark" value="Take Exam"> </form>')
    
    '''
    completed = tables.BooleanColumn(empty_values=(),
                                verbose_name='Completed')
    
    '''
    def __init__(self, *args, **kwargs):
        super(StudentAssesmentTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    def render_row_number(self):
        return '%d' % next(self.counter)
    
    
    '''
    def render_completed(self,value):
       return '%s' % value
    
    def render_total_exam_duration(self,value):
        return '%s' % value
    '''    
    
    def render_brief(self,value):
        return (value[:75] + '..') if len(value) > 75 else value
    
   
    class Meta:
        model = Assesment
        sequence = ( 'header','exam_start_date_time','passing_marks','privilege','expired_on')
        # add class="paleblue" to <table> tag 
        attrs = {'class': 'paleblue'}
        # fields = ( 'institute',)
        exclude = ('id', 'deleted_at','brief', 'privilege','deleted_by','created_by','updated_by','type','exam_start_type', 'polymorphic_ctype','created','updated','slug','is_exam_active')
