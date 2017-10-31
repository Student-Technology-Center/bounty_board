from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='bounty-board-index'),
    url(r'^add/$', views.bounty_board_add, name='bounty-board-add'),
    url(r'^delete/$', views.bounty_board_delete, name='bounty-board-delete'),
    url(r'^bounty/$' views.bounty_board_ticket, name='bounty-board-bounty'),
]