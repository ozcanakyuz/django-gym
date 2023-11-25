from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


from gym_site import settings
import home

urlpatterns = [
    path('', include('home.urls')),     #! random url result
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),

    #? blog pages
    path("about/", home.views.about, name="about"),
    path("feature/", home.views.feature, name="feature"),
    path("classes/", home.views.classes, name="classes"),
    path("contact/", home.views.contact, name="contact"),
    path("blog/", home.views.blog, name="blog"),
    path("single/", home.views.single, name="single"),

    path("signup/", home.views.signup_view, name="signup"),


    #? for the ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# To display images or static files on the admin side
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)