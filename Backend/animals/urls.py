from django.urls import path
from . import views

urlpatterns = [
    # path('test/<int:animal_id>/<int:order_id>/', views.AnimalsTestView.as_view()),
    # path('eat/', views.AnimalsEatView.as_view()),
    # path('play/wordchain/', views.AnimalsPlayWordChainView.as_view()),
    # path('play/newgame/', views.AnimalsPlayNewGame.as_view()),
    # path('talk/', views.AnimalsTalkView.as_view()),
    # path('color/', views.AnimalsColorView.as_view()),
    path('rename/', views.AnimalsRenameView.as_view()),
]