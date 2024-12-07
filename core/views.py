from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, UpdateView, DeleteView
from .services import createContextDictionary
from django.shortcuts import render, redirect
from .models import Response
from .forms import ResponseForm
from django.utils import timezone  ## Used by update view
from django.contrib.auth.mixins import LoginRequiredMixin ## Used by update view

# Create your views here.

# Table of Contents
#   Prepare context dictionary
#   Static Pages
#   RestAPIconsume
#   Create views
#   Read views
#   Update views
#   Delete views

###################################################################
# Prepare context dictionary in services.py for the sake of space.#
# A dictionary is returned when you call createContextDictionary()#
###################################################################


################
# Static views #
################
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    #This overide ensured the view gets fresh data every time it is rendered.
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return createContextDictionary()

# class HomePageView(TemplateView):
#     template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'pages/info/about.html'

class HasVoted(TemplateView):
    template_name = 'pages/info/iscreated.html'

class HasNotVoted(TemplateView):
    template_name = 'pages/info/isnotcreated.html'


##########
# Create #
##########

# Class-Based View(CVB) example
# A Class-Based View extends the View class. Requests are handled inside class methods named after
# the HTTP methods (GET, POST, PUT, HEAD ect.) offering SUPERIOR flexability.
class CreateCBView(View):

    # Renders the base HTML.
    def render(self, request):
        return render(request, 'pages/create.html',  {'form': ResponseForm})

    # Renders the Create form, if user is 1) logged in and 2) has not already voted.
    def get(self, request):

        # Redirect non-user to the all-auth sign up page. You must have account to Vote.
        if self.request.user.is_authenticated:
            pass
        else:
            return redirect('account_signup')

        PrevResponse = Response.objects.filter(created_by=self.request.user) # Query with a WHERE clause.
        if PrevResponse.exists():      # Redirect users who have already voted away from the Create page.
            return redirect('created')

        self.form = ResponseForm()  # Render requested Create form.
        return self.render(request)


    def post(self, request):

        self.form = ResponseForm(request.POST)

        if self.form.is_valid():
            self.form = self.form.save(commit=False) #This is the trick to saving editing input b4 commit.
            self.form.created_by = self.request.user
            self.form.save()
            return redirect('read')
            
        return self.render(request)


# Generic Class-Based View (GCBV) example of a CreateView.
class CreateGCBView(CreateView):
    model = Response
    form_class = ResponseForm
    template_name = 'pages/create.html'
    success_url = 'pages/read.html'
   
    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Saving user UUID to the Responce.

        # Assert user is logged in.
        if self.request.user.is_authenticated:  
            pass
        else:
            return redirect('account_signup')

        # Assert user vote will be unique
        PrevResponse = Response.objects.filter(created_by=self.request.user) # Query with a WHERE clause.
        if PrevResponse.exists():
            return redirect('created')

        # Return the object that form_valid wants, as in ccvb.uk
        return super(CreateGCBView, self).form_valid(form)


########
# Read #
########
class DetailView(TemplateView):
    model = Response
    # context_object_name = 'response_list' #Name of object in HTML template.
    template_name = 'pages/read.html'

    #This overide ensured the view gets fresh data every time it is rendered.
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        return createContextDictionary()



##########
# Update #
##########

# Class-Based View(CVB)   Out of order.
#  A Class-Based View extends the View class. Requests are handled inside class methods named after
#  the HTTP methods (GET, POST, PUT, HEAD ect.) offering SUPERIOR flexability.
class UpdateCBView(View):

    
    def render(self, request):

        # Assert the user is logged in. If the user is not logged in, redirect them to account login page.
        if self.request.user.is_authenticated:
            pass
        else:
            return redirect('account_signup')

        # Assert the user has a Response to update in the first place. 
        # If they do not have a Response, redirect them to a page explaining they need to submit a response first.
        # If they do have a Response, finally render the Update From.  
        PrevResponse = Response.objects.filter(created_by=self.request.user)
        if PrevResponse.exists() == 0:
            return redirect('notcreated')
        else:
            return render(request, 'pages/update.html',  {'form': ResponseForm})

    #This function retrieves the form itself and brings it to the page.
    def get(self, request):
        self.form = ResponseForm()
        return self.render(request)

    def post(self, request):

        #Delete the existing users previous entry.
        Response.objects.filter(created_by=self.request.user).delete()

        #Post the form data to the Django server.
        self.form = ResponseForm(request.POST)

        #If the form is valid, let's manipulate the data before saving.
        if self.form.is_valid():
            self.form = self.form.save(commit=False) #This is the trick to saving additional data.
            self.form.created_by = self.request.user #Data manipulation.
            self.form.save()                         #Save(commit) the data.
            return redirect('read')                  #Send the users to the DetailView upon submission.
            
        return self.render(request)


# Generic Class Based View (GCVB) UpdateCBView is NOT yet functional. 
# The Class Based View (CVB) implementation of a UpdateCBView above is functional.
class UpdateGCBView(LoginRequiredMixin, UpdateView):
    model = Response
    form_class = ResponseForm
    template_name = 'pages/update.html'
    pk_url_kwarg ='created_by'
    context_object_name = 'Response'
    success_url ="pages/read.html"

    #Validate the unser has a response before proceeding with the GET request. 
    def get(self, request, *args, **kwargs):

        # Assert the user has a Response to update in the first place. 
        # If they do not have a Response, redirect them to a page explaining they need to submit a response first.
        # If they do have a Response, finally render the Update From.  
        PrevResponse = Response.objects.filter(created_by=self.request.user)
        if PrevResponse.exists() == 0:
            return redirect('notcreated')
        else:
            self.object = self.get_object()
            return super().get(request, *args, **kwargs)

    # This method takes a query that tells UpdateView what object we are updating.
    def get_object(self):
        return Response.objects.get(created_by=self.request.user)

    #need to add form is not valid function
    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_at = timezone.now()
        post.save()
        return redirect('read')
    

##########
# Delete #
##########

# Class-Based View(CVB)
#  A Class-Based View extends the View class. Requests are handled inside class methods named after
#  the HTTP methods (GET, POST, PUT, HEAD ect.) offering SUPERIOR flexability.
class DeleteCBView(View):

    # Renders boilerplate HTML 
    def render(self, request):

        if self.request.user.is_authenticated:  # Assert user is logged in.
            pass
        else:
            return redirect('account_signup')

        return render(request, 'pages/delete.html')

    # Renders the delete form
    def get(self, request):
        return self.render(request)


    def post(self, request):

        #Delete the existing users previous entry upon delete.
        Response.objects.filter(created_by=self.request.user).delete()

        #return self.render(request)
        return render(request, 'pages/read.html',  {'response': Response})

# Generic Class Based View (GCVB) DeleteCBView is NOT yet functional. 
# The Class Based View (CVB) implementation of a DeleteCBView functional.
class DeleteGCBView(DeleteView):
    model = Response
    success_url ="pages/read.html"