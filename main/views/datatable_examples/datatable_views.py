from django.views.generic.list import ListView

from main.models import Person


class PersonListView(ListView):
    model = Person
    queryset = Person.objects.filter(pk__lte=10000)
    # paginate_by = 10
    template_name = 'main/datatable_examples/datatable_long_load.html'
