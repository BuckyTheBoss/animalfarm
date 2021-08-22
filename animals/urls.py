from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add_family', views.add_family, name='add_family'),
    path('update_family/<int:id>', views.update_family, name='update_family'),
    path('show_animals', views.AnimalListView.as_view(), name = 'all_animals'),
    path('show_animals/<int:pk>', views.AnimalDetailView.as_view(), name = 'animal_detail'),
    path('add_animal', views.AnimalCreateView.as_view(), name = 'create_animal'),
    path('update_animal/<int:pk>', views.AnimalUpdateView.as_view(), name = 'update_animal'),
    path('delete_animal/<int:pk>', views.AnimalDeleteView.as_view(), name = 'delete_animal'),
]