from home.models import HomePage
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        instance = HomePage.objects.first()
        data["object"] = instance
        return data
