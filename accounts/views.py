# Django REST Framework의 내장된 뷰들을 활용
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
def passwordResetRedirect(request, uid, token):
  return redirect(f"http://localhost:3000/password/reset/confirm/{uid}/{token}/")

def passwordResetDoneRedirect(request):
  return redirect(f"http://localhost:3000/")