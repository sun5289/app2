# polls/urls
from django.conf.urls import url
from . import views

app_name = 'polls' #여러 앱을 사용할시 html의 url를 사용시 name의 이름이 다른 앱과 중복될수있다. 네임 스페이스의 중복을 맞기위하여 사용한다.
                   # index.html 에 {% url 'polls:detail' question.id  %} 이렇게 사용하여 다른 앱과의 네임스페이스 중복을 막는다.
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
