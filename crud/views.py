from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import PersonForm
from .models import Person
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

        return redirect("home")

    else:
        form = PersonForm()

    return render(request, "forms.html", {"form": form})



def update_view(request, id):
    
    person = get_object_or_404(Person, id = id)

    if request.method == "POST":
             
        form = PersonForm(request.POST, instance=person)

        if form.is_valid():
            form.save()

            return redirect("home")

                 
    else:    
        form = PersonForm(instance=person)

    return render(request, "forms.html", {"form": form})


def retrieve_view(request):
    
    persons = Person.objects.all()

    return render(request, "retrieve.html", {"data":persons})




def detail_view(request, id):
    
    persons = Person.objects.get(id = id)

    return render(request, "detail.html", {"data":persons})



def home(request):
    return render(request, "home.html")