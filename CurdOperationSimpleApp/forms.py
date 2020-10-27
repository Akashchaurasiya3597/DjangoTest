from django import forms
class StudentForm(forms.Form):
    Roll_number = forms.IntegerField(
        label= 'Enter Student Roll Number',
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Roll Number'
            }
        )
    )
    First_name = forms.CharField(
        label='Enter Student First_name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Roll Number'
            }
        )
    )
    Last_name = forms.CharField(
        label='Enter Student Last Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }
        )
    )
    Email = forms.EmailField(
        label='Enter Student Email ID',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    School_name = forms.CharField(
        label='Enter Student School name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'School name'
            }
        )
    )
    Class_name = forms.CharField(
        label='Enter Student Class name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Class name'
            }
        )
    )
    Section_name = forms.CharField(
        label= 'Enter Student Section name',
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Section name'
            }
        )
    )
    Telugu_marks = forms.IntegerField(
        label='Enter Student Telugu Marks',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Telugu_marks'
            }
        )
    )
    Hindi_marks = forms.IntegerField(
        label='Enter Student Hindi Marks',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Hindi Marks'
            }
        )
    )
    English_marks = forms.IntegerField(
        label='Enter Student English marks',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'English Marks'
            }
        )
    )
    Maths_marks = forms.IntegerField(
        label='Enter Student Maths Marks',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Maths Marks'
            }
        )
    )
    Science_marks = forms.IntegerField(
        label='Enter Student Science Marks',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Science Marks'
            }
        )
    )
    Social_marks = forms.IntegerField(
        label='Enter Student Social Marks',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Science Marks'
            }
        )
    )

class StudentupdateForm(forms.Form):
    Roll_number = forms.IntegerField(
        label= 'Enter Student Roll Number',
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Roll Number'
            }
        )
    )
    Section_name = forms.CharField(
        label='Enter Student Section name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Section name'
            }
        )
    )

class StudentDeleteForm(forms.Form):
    Roll_number = forms.IntegerField(
        label= 'Enter Student Roll Number',
        widget= forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Roll Number'
            }
        )
    )