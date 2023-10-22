from django.urls import path
from . import views as v

urlpatterns=[
    path('about',v.about,name='about'),
    path('register',v.register,name='register'),
    path('login',v.loginn,name='loginn'),
    path('logout',v.logoutt,name='logoutt'),
    path('explore/<int:eid>',v.explore,name='explore'),
    path('userhome',v.userhome,name='userhome'),
    path('book/<int:eid>',v.booking,name='booking'),
    path('viewbooking',v.viewbooking,name='viewbooking'),
    path('edit/<int:eid>',v.edit,name='edit'),
    path('delete/<int:eid>',v.delete,name='delete'),
    path('search',v.search,name='search'),
    # path('delete1/<int:eid>',v.delete1,name='delete1'),




]