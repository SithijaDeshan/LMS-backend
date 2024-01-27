from django.urls import path, include
from rest_framework import routers
from LMS import views

router = routers.DefaultRouter()

router.register(r'userform', views.UserView, basename='userform')
router.register(r'booksform', views.BooksView, basename='booksform')

urlpatterns = [
    path('LMS/', include(router.urls))
]
