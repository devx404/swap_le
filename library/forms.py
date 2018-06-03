from django import forms
from .models import LibraryAsset
from students.models import Student

class LibraryAssetForm(forms.Form):
    ASSET_TYPE_CHOICES = (
        ('book ','BOOK'),
        ('cd','CD'),
        ('dvd','DVD')
        )
    
    asset_unique_code = forms.CharField(widget=forms.TextInput, required=True,label="Asset Unique Code")
    name = forms.CharField(widget=forms.TextInput, required=True,label="Asset Name")
    asset_type = forms.ChoiceField(choices=ASSET_TYPE_CHOICES, required=True,label="Asset Type")
    asset_description = forms.CharField(widget=forms.Textarea, required=True,label="Asset Description")
    
    

class LibraryAssetEditForm(forms.ModelForm):
    ASSET_TYPE_CHOICES = (
        ('book ','BOOK'),
        ('cd','CD'),
        ('dvd','DVD')
        )
    
    asset_unique_code = forms.CharField(widget=forms.TextInput, required=True,label="Asset Unique Code")
    name = forms.CharField(widget=forms.TextInput, required=True,label="Asset Name")
    asset_type = forms.ChoiceField(choices=ASSET_TYPE_CHOICES, required=True,label="Asset Type")
    asset_description = forms.CharField(widget=forms.Textarea, required=True,label="Asset Description")
    
    class Meta():
        model = LibraryAsset
        fields = ['asset_unique_code','name','asset_type','asset_description']
        
        
        
class AddLibraryAssetHistoryForm(forms.Form):
    student_id = forms.ModelChoiceField(queryset=Student.objects.all(),label="Student ID",required=True)
    
    def __init__(self, *args, **kwargs):
        super(PlaceEventForm, self).__init__(*args, **kwargs)
        self.fields['student_id'].queryset = Student.objects.filter(created_by=request.user)
    
    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super(AddLibraryAssetHistoryForm, self).__init__(*args, **kwargs)
        self.fields["student_id"].queryset = Student.objects.filter(staffuser__institute = self.request_user.staff.institute)
        
        
        
        