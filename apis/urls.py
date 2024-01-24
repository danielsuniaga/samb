from django.contrib import admin

from django.urls import path

from apis import views

urlpatterns = [

    path('test-endpoint/', views.TestEndPoint.as_view()),

    path('get-data-analysis-iqoption/', views.GetDataAnalysisIqOption.as_view())

]