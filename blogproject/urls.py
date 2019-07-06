"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.main, name="main"),
    path('input/', blog.views.input, name="input"),
    path('savedata/', blog.views.savedata, name="savedata"),
    path('update_page/<int:id>', blog.views.update_page, name="update_page"),
    path('update/<int:id>', blog.views.update, name="update"),
    path('delete/<int:id>', blog.views.delete, name="delete"),
    path('detail/<int:id>', blog.views.detail, name="detail"),
    path('comment_save/<int:id>', blog.views.comment_save, name="comment_save"),
    path('comment_delete/<int:comment_id>', blog.views.comment_delete, name="comment_delete"),
    path('comment_update_page/<int:comment_id>', blog.views.comment_update_page, name="comment_update_page"),
    path('comment_update/<int:comment_id>', blog.views.comment_update, name="comment_update"),
    path('sign_in/', blog.views.sign_in, name="sign_in"),
    path('sign_up/', blog.views.sign_up, name="sign_up"),
    path('sign_out/', blog.views.sign_out, name="sign_out"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

