from django.views import generic
from .models import Article, Comment
from .forms import IndexPageForms, ArticleForm, CommentForm
from django.core.urlresolvers import reverse
from django.http import Http404,HttpResponseRedirect
from django.db.models import Count
from django.shortcuts import get_object_or_404

class DetailView(generic.DetailView):
    model = Article
    template_name = "main_blog/detail.html"

    def dispatch(self, request, *args, **kwargs):
        self.comment_form = CommentForm()
        return super(DetailView, self).dispatch(request,*args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context["comment_form"] = self.comment_form
        return context

class AddNewArticle(generic.CreateView):
    form_class = ArticleForm
    #fields = ("article_title","article_text")
    template_name = "main_blog/add_new_article.html"
    model = Article

    # auto author adding
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddNewArticle,self).form_valid(form)


    # form.instance - генерируемый объект
    # form_valid() - функция вызываемая при успешной валидации/создании объекта

class IndexList(generic.ListView):
    template_name = "main_blog/index.html"
    model = Article

    # {% url "main_blog:detail" article.id %}
    # {% url "name" aaas %} - подставляет ссылку под именем name с переменной aaas

    def dispatch(self, request, *args, **kwargs):
        self.form = IndexPageForms(request.GET)
        self.form.is_valid()
        # Возвращает False если валидация прошла не успешно.
        return super(IndexList, self).dispatch(request,*args,**kwargs)
    # переопределяет dispatch - он стартует в начале, вродь

    def get_queryset(self):

        sort_field = self.form.cleaned_data.get("sort_field")
        search_field = self.form.cleaned_data.get("search")
        # Возвращает отвалидированные данные, или None если они не прошли проверку

        if sort_field == '' or sort_field == None:
            sort_field = "-pub_date"

        if search_field == None:
            search_field = ''
        # значение по умолчанию / если не задан sort_field



        self.queryset = Article.objects.all().order_by(sort_field)
        # сортировка по умолчанию

        if sort_field == "comments_count":
            self.queryset = self.queryset.annotate(comments_count=Count("comment__id")).order_by("-comments_count")
             # считает объекты comment's для каждого из article из queryset и ложит значение в comments_count
             # https://djbook.ru/rel1.9/topics/db/aggregation.html

        if search_field != "":
            self.queryset = self.queryset.filter(article_title__icontains=search_field)

        return self.queryset[0:60]
    # get_queryset - получить список объектов для отображения.

    def get_context_data(self, **kwargs):
        context = super(IndexList, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context

class AddNewComment(generic.CreateView):
    form_class = CommentForm
    model = Comment
    def dispatch(self, request, *args, **kwargs):
        self.success_url = reverse("main_blog:index")
        # Значение по умолчанию, как минимум так задумывается.
        return super(AddNewComment, self).dispatch(request)

    def form_invalid(self, form):
        raise Http404


    def form_valid(self, form):
        form.instance.author = self.request.user
        for iter_object in Article.objects.all().filter(pk=self.request.POST.get("pk")):
            form.instance.article = iter_object
        self.success_url = self.request.POST.get("next")

        return super(AddNewComment, self).form_valid(form)

def add_rating_for_article(request):
    article_id = request.POST.get("article_id")
    article = get_object_or_404(Article, pk=article_id)
    user = request.user
    if not article.article_rating.filter(pk=user.pk):
        article.article_rating.add(user)
    else:
        article.article_rating.remove(user)
    return HttpResponseRedirect(request.POST.get("next"))




