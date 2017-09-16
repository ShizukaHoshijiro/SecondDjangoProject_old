
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
from django.conf import settings

# ?P<question_id> - передвёт отображению переменную question_id
# [0-9]+ - распознаёт цифры
# В скобках- значит передать переменную

# redirect after login
settings.LOGIN_REDIRECT_URL = "login.html"

app_name = "main_blog"
urlpatterns = [
    url(r"^$", views.IndexList.as_view(), name="index"),
    #exp: /
    url(r"^(?P<pk>[0-9]+)/$", views.DetailView.as_view(), name="detail"),
    #exp: /43/
    url(r"^add/$", views.AddNewArticle.as_view(), name="add"),
    #exp: /add/
    url(r"^addcomment/$", views.AddNewComment.as_view(), name="add_comment"),
    url(r"^login/$", login, {"template_name": "main_blog/login.html"}, name="login"),
    url(r"^logout/$", logout, name="logout"),
    url(r"^add_rating/$", views.add_rating_for_article, name="add_rating"),
]

