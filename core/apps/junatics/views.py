from django.shortcuts import render

from core.apps.junatics.models import Junatics
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'junatics/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['junatics'] = Junatics.objects.all()
        return context


