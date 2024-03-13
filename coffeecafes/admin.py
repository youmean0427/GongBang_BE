from django.contrib import admin
from coffeecafes.models import CoffeeCafe, Review, CoffeeCafeImage, ReviewImage

# Django Rest Framework Model
admin.site.register(CoffeeCafe)
admin.site.register(Review)
admin.site.register(CoffeeCafeImage)
admin.site.register(ReviewImage)
