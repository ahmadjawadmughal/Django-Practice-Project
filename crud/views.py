from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import PersonForm
from .models import Person
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import gettext as _
from django.views.generic import ListView
import datetime
from django.utils.timezone import now
# Create your views here.


def create_view(request):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            country = form.cleaned_data["country"]
            age = form.cleaned_data["age"]

            #Person.objects.create(name= name, age= age, email = email, phone_on = phone_no, country = country)
            person = Person(name= name, 
                             age= age, 
                             email = email, 
                             country = country)
            person.save()

        return redirect("retrieve-view")

    else:
        form = PersonForm()

    return render(request, "forms.html", {"form": form})



def update_view(request, id):
    
    person = get_object_or_404(Person, id = id)

    if request.method == "POST":
             
        form = PersonForm(request.POST, instance=person)

        if form.is_valid():
            form.save()

            messages.success(request, "Person is Updated successfully!")
            return redirect("detail-view", id= person.id)

                 
    else:    
        form = PersonForm(instance=person)

    messages.success(request, "Updating the person data is failed!")
    return render(request, "forms.html", {"form": form})


def retrieve_view(request):
    
    persons = Person.objects.all()
    page_num = request.GET.get('page', 1)
   
    paginator = Paginator(persons, 2)
    
    page_obj = paginator.get_page(page_num)

    return render(request, "retrieve.html", {"users":page_obj})

"""
class UserListView(ListView):
    model = Person
    template_name = "retrieve.html"
    context_object_name = "users"
    paginate_by = 5
    persons = Person.objects.all()
"""


def detail_view(request, id):
    
    persons = Person.objects.get(id = id)

    return render(request, "detail.html", {"data":persons})


def delete_view(request, id):
    
    obj = get_object_or_404(Person, id= id)
    
    if request.method == "POST":
        
        obj.delete()  
        
        messages.success(request, f"{obj.name} is deleted successfully!")
        return redirect("retrieve-view")
    
    
    return render(request, 'delete_confirmation.html', {"object": obj})

def home(request):

    today = datetime.date.today()
    return render(request, "home.html", {"today": today, "now": now()})


