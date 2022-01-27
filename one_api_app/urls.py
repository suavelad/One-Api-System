from django.urls import path
from .apis import  GetAllCharactersView,GetQuotePerCharactersView,GetQuotePerMoviesView,\
    GetAllMoviesView,GetAllQuotesView,GetAllChaptersView,GetQuotePerIdView,GetMoviePerIdView,GetChapterPerIdView
from rest_framework.routers import DefaultRouter
 
router = DefaultRouter()


# router.register('category',CategoryViewSet, 'category')

urlpatterns = router.urls

urlpatterns += [
    path('get/all/character/',GetAllCharactersView.as_view(), name="get-all-characters"),
    path('get/all/movie/',GetAllMoviesView.as_view(), name="get-all-movies"),
    path('get/all/quote/',GetAllQuotesView.as_view(), name="get-all-quotes"),
    path('get/all/chapter/',GetAllChaptersView.as_view(), name="get-all-chapters"),
    

    path('get/character/<id>/quote/',GetQuotePerCharactersView.as_view(), name='get-quote-per-character'),
    path('get/movie/<id>/quote/',GetQuotePerMoviesView.as_view(), name='get-quote-per-movie'),

    path('get/quote/<id>/',GetQuotePerIdView.as_view(), name='get-quote-per-id'),
    path('get/movie/<id>/',GetMoviePerIdView.as_view(), name='get-movie-per-id'),
    path('get/chapter/<id>/',GetChapterPerIdView.as_view(), name='get-chapter-per-id'),


    # path('update/extracted_data/',GetUpdateExtractedDataView.as_view(), name='update_extracted_data'),
]