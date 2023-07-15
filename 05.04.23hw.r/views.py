from django.views.generic import ListView
from .models import Rating

class RatingListView(ListView):
    model = Rating
    template_name = 'ratings/rating_list.html'
    context_object_name = 'ratings'
