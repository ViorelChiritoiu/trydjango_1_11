import random
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        num = random.randint(0, 100)
        some_list = [
            num,
            random.randint(0, 10),
            random.randint(0, 1000)
        ]
        context = {
            "html_var": True,
            "num": num,
            "some_list": some_list
        }
        return context
