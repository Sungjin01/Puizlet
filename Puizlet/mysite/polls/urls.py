from django.urls import path
from polls import views


app_name='polls'

urlpatterns=[
    
    path('', views.main, name='main'),
    path('makebooks/<int:latest_wordbook_id>/', views.makebooks, name = 'makebooks'),
    path('<int:wordbook_id>/', views.words, name='words'),
    path('<int:wordbook_id>/makewords/', views.makewords, name = 'makewords'),
    path('study/<int:wordbook_id>/<int:cnt>/', views.study, name='study'),
    path('result/<int:cnt>/', views.result, name='result'),
    path('check/<int:wordbook_id>/<str:eng_word>/<int:cnt>/', views.check, name='check'),
    path('remove/<int:wordbook_id>/', views.remove, name='remove'),
    path('removeword/<int:word_id>/', views.removeword, name='removeword'),
]