from django.urls import path

from main.views.datatable_examples.datatable_views import PersonListView


urlpatterns = [
    path('', PersonListView.as_view(), name='datable-example-person-list')
]
