
from django import forms
from .models import Article, Comment


class IndexPageForms(forms.Form):
    search = forms.CharField(required=False)
    sort_field = forms.ChoiceField(choices=(("-pub_date","Дата создания"),("-article_rating","Рейтинг"),("comments_count","Количество комментариев")),required=False)
# Формы сортировки

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["article_title","article_text"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text"]
        widgets = {
            'comment_text': forms.Textarea(attrs={'cols': 66, 'rows': 6, "placeholder":"Напишите комментарий." }),
        }




