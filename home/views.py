from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect

from .forms import PersonForm
from .models import Person



class HomeView(View):
    def get(self, request):
        # Get people from db
        people = Person.objects.all()

        form = PersonForm()
        context = {
            'form': form,
            'people': people,
        }
        return render(request, 'home/home.html', context)

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            people = Person.objects.all()
            context = {
                'form': form,
                'people': people,
            }
            return render(request, 'home/home.html', context)


class PersonDetail(View):
    def get(self, request, pk):
        person = get_object_or_404(Person, pk=pk)
        context = {
            'person': person,
        }
        return render(request, 'home/person_detail.html', context)