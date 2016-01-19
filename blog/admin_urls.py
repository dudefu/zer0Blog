from django.conf.urls import url,include

from blog.admin_views import PostView, DeletePost, NewPost, UpdatePostIndexView, AddPost, \
    UpdateDraft, UpdatePost, UpdateEditor, LogoutView, CarouselIndexView, CarouselEditView, \
    AddCarousel, DeleteCarousel, CarouselUpdateView, updateCarousel

urlpatterns = [
    url(r'^admin/', include([
        url(r'^$', PostView.as_view(), name='index'),
        url(r'^delete/(?P<pk>[0-9]+)$', DeletePost.as_view()),
        url(r'^new$', NewPost.as_view()),
        url(r'^add$', AddPost.as_view()),
        url(r'^update/draft/(?P<pk>[0-9]+)$', UpdateDraft.as_view()),
        url(r'^update/post/(?P<pk>[0-9]+)$', UpdatePost.as_view()),
        url(r'^update/(?P<pk>[0-9]+)$', UpdatePostIndexView.as_view()),
        url(r'^update/editor$', UpdateEditor.as_view()),
        url(r'^carousel$', CarouselIndexView.as_view()),
        url(r'^update/carousel$', CarouselEditView.as_view()),
        url(r'^add/carousel$', AddCarousel.as_view()),
        url(r'^delete/carousel/(?P<pk>[0-9]+)$', DeleteCarousel.as_view()),
        url(r'^update/carousel/(?P<pk>[0-9]+)$', CarouselUpdateView.as_view()),
        url(r'^update/carousel/id/(?P<pk>[0-9]+)$', updateCarousel.as_view()),
        url(r'^repository$', PostView.as_view(), name='index'),
        url(r'^set$', PostView.as_view(), name='index'),
        url(r'^logout$', LogoutView.as_view()),
    ])),
]