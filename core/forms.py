from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Response

#These forms create objects specified in the meta felid. We can change attributes on our form
# from here in python. 
class ResponseForm(forms.ModelForm):        

    # Crispy forms initializer
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'POST'
        self.helper.form_action = 'submit'
        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['Question1'].label = "What is your favorite season?"

        
    #Basic Model Form Meta subclass. We use the felids parameter to manage the order of what is displayed.
    class Meta:
        model = Response
        fields = [
            'Question1',
        ]
        
        # Use this as the felids attribute when you want to the form to display
        # inputs for all felids in a object. 

        #fields = '__all__' #Use all model fields