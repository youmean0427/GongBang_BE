from django.contrib import admin
from coffeecafes.models import CoffeeCafe, Review, CoffeeCafeImage, ReviewImage, RecoCafe
from accounts.models import User
# Django Rest Framework Model
admin.site.register(CoffeeCafe)
admin.site.register(Review)
admin.site.register(CoffeeCafeImage)
admin.site.register(ReviewImage)
admin.site.register(RecoCafe)
admin.site.register(User)

