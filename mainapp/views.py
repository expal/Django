from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from mainapp import models


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = models.News.objects.all()[:5]
        return context_data


class NewsPageDetailView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, pk=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["news_description"] = get_object_or_404(models.News, pk=pk)
        return context_data


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"
    # Create your views here.
