from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^blogTop5/$', views.top_posts),
    url(r'^blog/(?P<db_id>\d+)/$', views.post_detail),
]
