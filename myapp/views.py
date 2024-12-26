from django.http import HttpResponse, Http404
from django.views.generic.base import TemplateView, RedirectView
import datetime
from django.contrib.auth.hashers import make_password, check_password, is_password_usable
from django.contrib.auth.password_validation import validate_password,password_changed
from django.shortcuts import render, get_object_or_404
from .models import Student

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the myapp index.")

def get_name(request, name):
    return render(request, "tempview.html", {"name": name})

def extra_option(request, extra_option):
    return HttpResponse(f"extra option: {extra_option}")

def current_datetime(request):
    
    date = datetime.datetime.now()
    
    return render(request, "index.html", {"date": date})


def get_students(request):
        
    try:    
        st = Student.objects.get(id = 1)
        return HttpResponse(st.name)
    
    except Student.DoesNotExist:
        raise Http404("This Student Not Exist!")
        # return HttpResponse("<p>Not exist!</p>")


#Class based views   

class TempView(TemplateView):

    # template_name inherited from the TemplateRespnseMixin class

    template_name = "tempview.html"


    # inherited from the ContextMixin class

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['st_name'] = Student.objects.filter(name__contains = "Os").first()
        print(context["st_name"])
        context['data'] = "This is a template view."

        return context
    


class Rd(RedirectView):

    pattern_name = "single-student"  # this "tempview" comes from the name attribute of the url

    def get_redirect_url(self, *args, **kwargs):

        student = get_object_or_404(Student, pk=kwargs['pk'])
        student.name = "johnny"  #update
        student.save()
     

        return super().get_redirect_url(*args, **kwargs)


class SingleStudent(TemplateView):

    template_name = "tempview.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['st_name'] = get_object_or_404(Student, pk=self.kwargs.get('pk'))

        return context
    


password = make_password("hello")
check = check_password("hello", password)
print(check) # false
validate  = validate_password(password)
print("validate: ", validate) # if valid, return None
usable = is_password_usable(password)
print(usable)

changed = password_changed("changed")
print(changed)