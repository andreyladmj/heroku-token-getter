from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views
import hello.views_oauth

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    # path("callback/", hello.views.callback, name="callback"),
    # path("check_code/", hello.views.check_code, name="check_code"),

    path("oauth/csrf_form_html/", hello.views_oauth.csrf_form_html, name="csrf_form_html"),
    path("oauth/client/", hello.views_oauth.client, name="views_oauth.client"),
    path("oauth/get_token/", hello.views_oauth.get_token, name="views_oauth.get_token"),
    path("oauth/autosubmit_forms/", hello.views_oauth.autosubmit_forms, name="views_oauth.autosubmit_forms"),
    path("oauth/autosubmit_iframe/", hello.views_oauth.autosubmit_iframe, name="views_oauth.autosubmit_iframe"),

    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
