# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]

from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


app_name = 'streaming'

urlpatterns = [
    path('', views.home, name='home'),  # this is your user homepage
    # path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # admin panel
    path('register/', views.register, name='register'),
    path('signin/', views.signin_view, name='signin'),

    path('free/', views.free_page, name='free'),
    path('sortseries/', views.sort_series_page, name='sortseries'),
    path('kdrama/', views.kdrama_page, name='kdrama'),
    path('cdrama/', views.cdrama_page, name='cdrama'),
    path('thaidrama/', views.thaidrama_page, name='thaidrama'),
    path('reality-show/', views.reality_show_page, name='reality_show'),
    path('movies/', views.movies_page, name='movies'),
    path('anime/', views.anime_page, name='anime'),
    path('all/', views.all_page, name='all'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)