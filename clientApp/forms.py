from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from clientApp.models import (
    Client,
    Operator,
    Employee,
    Feedback,
    Leave,
    OperatorDocument,
    MessageQuery,
    Invoice,
    EmployeeDocument,
    EmployeeHoliday,
    EmployeeFeedback
)

CLIENT_TYPE = (
    ('', 'Choose...'),
    ('Taxi Firm', 'Taxi Firm'),
    ('Insurance Firm', 'Insurance Firm'),
    ('Others', 'Others')
)
RATING_CHOICES = (
    ('', 'Choose...'),
    ('One Star', 'One Star'),
    ('Two Star', 'Two Star'),
    ('Three Star', 'Three Star'),
    ('Four Star', 'Four Star'),
    ('Five Star', 'Five Star'),
)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
    )
    first_name = forms.CharField(
        required=True,
    )
    last_name = forms.CharField(
        required=True,
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'style': 'text-transform:lowercase;'})
    )

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class ClientRegistrationForm(forms.ModelForm):
    address = forms.CharField(
        max_length=150,
        required=True,
        label="Address",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter complete address'
        }),
    )
    contact_number = forms.CharField(
        required=True,
        label="Contact Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter contact number'
        }),
    )
    client_type = forms.ChoiceField(
        required=True,
        label="Client Type",
        choices=CLIENT_TYPE,
    )

    class Meta:
        model = Client
        fields = (
            'client_name',
            'client_type',
            'contact_number',
            'address',
            'profile_picture'
        )
        labels = {
            'client_name': 'Company Name'
            }


class OperatorRegistrationForm(forms.ModelForm):
    address = forms.CharField(
        max_length=150,
        required=True,
        label="Address",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter complete address'
        }),
    )
    contact_number = forms.CharField(
        required=True,
        label="Contact Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter contact number'
        }),
    )
    date_of_birth = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'format': 'd-m-Y', 'input_formats': 'd-m-Y'},
            
        )
    )

    class Meta:
        model = Operator
        fields = (
            'client_id',
            'contact_number',
            'date_of_birth',
            'address',
            'total_leaves',
            'profile_picture'
        )
        labels = {
            "total_leaves": "Total Holidays"
        }


class EmployeeRegistrationForm(forms.ModelForm):
    address = forms.CharField(
        max_length=150,
        required=True,
        label="Address",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter complete address'
        }),
    )
    contact_number = forms.CharField(
        required=True,
        label="Contact Number",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter contact number'
        }),
    )
    date_of_birth = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date', 'format': 'd-m-Y', 'input_formats': 'd-m-Y'},
            
        )
    )

    class Meta:
        model = Employee
        fields = (
            'job_designation',
            'contact_number',
            'date_of_birth',
            'address',
            'total_leaves',
            'profile_picture'
        )
        labels = {
            "total_leaves": "Total Holidays"
        }


class FeedbackForm(forms.ModelForm):
    rating = forms.ChoiceField(
        required=True,
        label="Rating",
        choices=RATING_CHOICES
    )

    def __init__(self, request,  *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['operator_id'].queryset = Operator.objects.filter(
            client_id=request.user.client.client_user_id)

    class Meta:
        model = Feedback
        fields = (
            'operator_id',
            'rating',
            'feedback_note'
        )
        labels = {
            "operator_id": "Operator Name"
        }


class LeaveForm(forms.ModelForm):
    from_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        label="From"
    )
    to_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        label="To"
    )

    class Meta:
        model = Leave
        fields = (
            'from_date',
            'to_date',
            'reason'
        )


class OperatorDocumentsForm(forms.ModelForm):
    documents = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'multiple': True
    }))

    class Meta:
        model = OperatorDocument
        fields = (
            'documents',
        )


class ClientSendMessageForm(forms.ModelForm):

    def __init__(self, request,  *args, **kwargs):
        super(ClientSendMessageForm, self).__init__(*args, **kwargs)
        self.fields['operator_id'].queryset = Operator.objects.filter(
            client_id=request.user.client.client_user_id)

    class Meta:
        model = MessageQuery
        fields = (
            'operator_id',
            'messageQuery'
        )
        labels = {
            "operator_id": "Operator Name",
            "messageQuery": "Message"
        }


class AdminSendMessageForm(forms.ModelForm):
    def __init__(self, request,  *args, **kwargs):
        super(AdminSendMessageForm, self).__init__(*args, **kwargs)
        self.fields['client_id'].queryset = Client.objects.all().order_by(
            'client_name')

    class Meta:
        model = MessageQuery
        fields = (
            'client_id',
            'messageQuery'
        )
        labels = {
            "client_id": "Client Name",
            "messageQuery": "Message"
        }


class AdminSendMessageToOperatorForm(forms.ModelForm):

    class Meta:
        model = MessageQuery
        fields = (
            'operator_id',
            'messageQuery'
        )
        labels = {
            "operator_id": "Operator Name",
            "messageQuery": "Message"
        }


class ClientSendMessageToAdminForm(forms.ModelForm):

    class Meta:
        model = MessageQuery
        fields = (
            'messageQuery',
        )
        labels = {
            "messageQuery": "Message"
        }


class ClientInvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = (
            'client_id',
            'title',
            'invoices'
        )
        labels = {
            "client_id": "Client Name",
        }


class EmployeeDocumentsForm(forms.ModelForm):
    documents = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'multiple': True
    }))

    class Meta:
        model = EmployeeDocument
        fields = (
            'documents',
        )


class EmployeeHolidayForm(forms.ModelForm):
    from_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        label="From"
    )
    to_date = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        ),
        label="To"
    )

    class Meta:
        model = EmployeeHoliday
        fields = (
            'from_date',
            'to_date',
            'reason'
        )


class EmployeeFeedbackForm(forms.ModelForm):
    rating = forms.ChoiceField(
        required=True,
        label="Rating",
        choices=RATING_CHOICES
    )

    class Meta:
        model = EmployeeFeedback
        fields = (
            'employee_id',
            'rating',
            'feedback_note'
        )
        labels = {
            "employee_id": "Employee Name"
        }
