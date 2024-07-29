from . import views
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('faqs/', views.contact_view, name='faqs'),
    path('berita/<int:id>', views.beritadetail,name="beritadetail"),
    path('berita/', views.berita,name="berita"),
    
    
    path("pendidikan_ma/",views.pendidikan_ma,name="pendidikan_ma"),
    path("pendidikan_smp",views.pendidikan_smp,name="pendidikan_smp"),
    path("pendidikan_mahad",views.pendidikan_mahad,name="pendidikan_mahad"),
    path("pendidikan_tpq",views.pendidikan_tpq,name="pendidikan_tpq"),
    path("pendidikan_kampus",views.pendidikan_kampus,name="pendidikan_kampus"),
    
    
    path('profil/', views.profil, name='profil'),
    path('struktur_organisasi/', views.struktur_organisasi, name='struktur_organisasi'),
    path('akreditasi/', views.akreditasi, name='akreditasi'),
    path('prestasi/', views.prestasi, name='prestasi'),
    path('pendidikan_ma/', views.pendidikan_ma, name='pendidikan_ma'),
    path('berita/', views.berita, name='berita'),
    path('faqs/', views.faqs, name='faqs'),
    path('helpdesk/', views.helpdesk, name='helpdesk'),
    path('ppdb/', views.ppdb, name='ppdb'),
]
