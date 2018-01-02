from django.shortcuts import render
from .models import RestaurantLocation
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .forms import RestaurantCreateForm

#
# def restaurant_list_view(request):
#     template_name = "restaurants/restaurants_list.html"
#     queryset = RestaurantLocation.objects.all()
#     context = {
#         "object_list": queryset,
#     }
#     return render(request, template_name, context)


class RestaurantListView(ListView):
    template_name = "restaurants/restaurants_list.html"

    def get_queryset(self):
        print(self.kwargs)
        slug = self.kwargs.get("slug")
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    template_name = "restaurants/restaurant_detail.html"
    queryset = RestaurantLocation.objects.all()

    # def get_context_data(self, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data()
    #     print(context)
    #     return context

    # def get_object(self, **kwargs):
    #     rest_id = self.kwargs.get("pk")
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj


def restaurant_create_form(request):
    if request.method == "GET":
        print("get data")
    if request.method == "POST":
        print("post data")
    template_name = "restaurants/form.html"
    context = {}
    return render(request, template_name, context)