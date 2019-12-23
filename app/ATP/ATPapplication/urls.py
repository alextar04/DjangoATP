from django.urls import path
from .views import *


urlpatterns = [
    path('', startPage, name='start'),
    path('login/', login, name='login_url'),
    path('logout/', logout, name='logout_url'),
    path('news/', allNews, name='all_news_url'),
    path('news/create/', createNews, name='news_create_url'),
    path('news/delete/<str:slug>', deleteNews, name='news_delete_url'),
    path('news/update/<str:slug>', updateNews, name='news_update_url'),
    path('news/<str:slug>/', currentNews, name='one_news_url'),
    path('player/', players, name='players_url'),
    path('player/update/<str:slug>', updatePlayer, name='player_update_url'),
    path('player/top10', playersTop10, name='players_url_top10'),
    path('player/top20', playersTop20, name='players_url_top20'),
    path('player/top30', playersTop30, name='players_url_top30'),
    path('player/counrty/<str:slug>', playersTopCountry, name='player_url_country'),
    path('player/<str:slug>/', currentPlayer, name='player_url'),
    path('info/', structure, name='info_url'),
    path('<str:slug>/', grandslam, name='grandslam_url'),
    path('<str:slug>/4round', fourRound, name='fourRound_url'),
    path('<str:slug>/quaterfinal', quaterfinal, name='quaterfinal_url'),
    path('<str:slug>/semifinal', semifinal, name='semifinal_url'),
    path('<str:slug>/final', final, name='final_url'),
    path('csv/<str:slug>', toCsv, name='convert_csv_url')
]