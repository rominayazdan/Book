from django.utils.deprecation import MiddlewareMixin

class BookRedirectMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info == "/book/view":
            request.path_info = "/book/see-books"