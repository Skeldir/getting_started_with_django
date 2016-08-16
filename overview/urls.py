from django.conf.urls import patterns, url

from overview import views

urlpatterns = patterns( "",
  url(r"^$", views.overview, name="overview"),
  url(r"^session$", views.session, name="session_overview"),
)

