from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm
from django.utils import timezone


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review/review.html', {'reviews': reviews})


def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'review/article-details.html', {'review': review})


def review_new(request):
    if request.method == "review":
        form = ReviewForm(request.review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.published_date = timezone.now()
            review.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm()
    return render(request, 'review/review_edit.html', {'form': form})


def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "review":
        form = ReviewForm(request.review, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.published_date = timezone.now()
            review.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'review/review_edit.html', {'form': form})


def review_remove(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('review_list')


