from django.http import HttpResponse
from django.views import View


class BookView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!")
