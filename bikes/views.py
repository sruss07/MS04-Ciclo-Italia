from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from .models import Bike, Brand
from reviews.models import BikeReview
from reviews.forms import BikeReviewForm


def all_bikes(request):
    """A view that shows all bikes,\
    with searching and sorting features """

    bikes = Bike.objects.all()
    query = None
    brand = None
    # Code used from Boutique Ado - CI Lesson
    if request.GET:
        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            bikes = bikes.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "No search request")
                return redirect(reverse('bikes'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            bikes = bikes.filter(queries)

    context = {
        'bikes': bikes,
        'search_bikes': query,
        'brand_range': brand,
    }

    return render(request, 'bikes/bikes.html', context)


def bike_detail(request, bike_id):
    """ A view to show an idividual bike and its user reviews. """

    bike = get_object_or_404(Bike, pk=bike_id)
    bike_reviews = BikeReview.objects.all().filter(bike=bike)
    bike_review_form = BikeReviewForm()

    context = {
        'bike': bike,
        'bike_reviews': bike_reviews,
        'bike_review_form': bike_review_form,
    }

    return render(request, 'bikes/bike_detail.html', context)
