from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.views.generic import RedirectView
import debug_toolbar

urlpatterns = i18n_patterns(
    path("", RedirectView.as_view(url=reverse_lazy("admin:index"))),
    path("admin/", admin.site.urls),
    path("admindocs/", include("django.contrib.admindocs.urls")),
    path("__debug__/", include(debug_toolbar.urls)),
)
