from django.urls import path
from .views import blog_view, blog_detail


app_name = 'blog'

<<<<<<< HEAD
urlpatterns = [

]
=======
urlpatterns = {
    path('blogslist/', blog_view, name='blog'),
    path('bloglist<slug:slug>/', blog_detail, name='detail'),
}
>>>>>>> origin/main
