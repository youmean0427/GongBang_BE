from django.urls import path
from . import views

urlpatterns = [
    # cafe
    path('coffeecafes/all/<int:type>', views.get_coffeecafes),
    path('coffeecafes/detail/<int:id>', views.get_coffeecafes_detail),
    path('coffeecafes/create', views.create_coffeecafe),

    # Review All
    path('coffeecafes/review', views.get_review_all),
    # Review Detail
    path('coffeecafes/review/<int:id>', views.get_review),
    # Review Create/Update
    path('coffeecafes/detail/<int:id>/review/<int:type>', views.post_coffeecafe_detail_review),
    # Review Delete
    path('coffeecafes/review/<int:id>/delete', views.delete_review),
    # Review Image Delete
    path('coffeecafes/review/image/<int:id>', views.delete_review_image),

    # Profile
    path('profile/<int:user_id>', views.profile),

    # RecoCafe
    path('coffeecafes/recommend', views.create_recocafe)
    
]