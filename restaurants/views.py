from django.shortcuts import render
from .models import RestaurantLocation
from django.views.generic import ListView
from django.db.models import Q


def restaurant_list_view(request):
    template_name = "restaurants/restaurants_list.html"
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, template_name, context)


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
#
#
# class SearchRestaurantListView(ListView):
#     template_name = "restaurants/restaurants_list.html"
#
#     def get_queryset(self):
#         print(self.kwargs)
#         slug = self.kwargs.get("slug")
#         if slug:
#             queryset = RestaurantLocation.objects.filter(
#                 Q(category__iexact=slug) |
#                 Q(category__icontains=slug)
#             )
#         else:
#             queryset = RestaurantLocation.objects.none()
#         return queryset