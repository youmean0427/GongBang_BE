# Django REST Framework의 내장된 뷰들을 활용
from coffeecafes.models import Review
from django.http import JsonResponse
from coffeecafes.serializers import ReviewSerializer
def profile(request, user_id):
  review = Review.objects.all()
  if request.method == 'GET':
      serializer_review = ReviewSerializer(review)
      return JsonResponse(serializer_review.data, safe=False)