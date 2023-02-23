from django.urls import path
from sell.views.base_views import *
from sell.views import profile_view, comment_view, writing_view, policies_view
from sell import webpush

app_name = 'sell'

urlpatterns = [
    path('', index, name='main'),
    path('list/<str:category_name>/', writing_view.writing_list, name='writing_list'),
    path('list/<str:category_name>/create/', writing_view.writing_create, name='writing_create'),
    path('list/<int:writing_id>/modify/', writing_view.writing_modify, name='writing_modify'),
    path('list/<int:writing_id>/delete/', writing_view.writing_delete, name='writing_delete'),
    path('list/detail/<int:writing_id>/', writing_view.writing_detail, name='writing_detail'),

    path('list/comment/create/<int:writing_id>/', comment_view.comment_create, name='comment_create'),
    path('list/comment/modify/<int:comment_id>/', comment_view.comment_modify, name='comment_modify'),
    path('list/comment/delete/<int:comment_id>/', comment_view.comment_delete, name='comment_delete'),
    path('list/reply_comment/create/<int:writing_id>/', comment_view.comment_create, name='reply_comment_create'),

    path('profile/', profile_view.profile, name="profile"),
    path('profile/mcomment/', profile_view.profile_mcomment, name="profile_mcomment"),
    path('profile/update/', profile_view.profile_update, name="profile_update"),
    path('profile/delete/', profile_view.profile_delete, name="profile_delete"),

    path('policies/user_agreement/', policies_view.user_agreement, name="user_agreement"),
    path('policies/privacy_policy/', policies_view.privacy_policy, name="privacy_policy"),
]
