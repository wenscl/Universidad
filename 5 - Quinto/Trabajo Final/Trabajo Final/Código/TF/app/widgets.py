from django.forms import DateInput


class DatePickerInput(DateInput):
    template_name = 'app/widget/datepicker.html'


class MonthDatePickerInput(DateInput):
    template_name = 'app/widget/month_datepicker.html'
