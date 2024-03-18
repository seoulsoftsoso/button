from django.db.models import ProtectedError
from django.http import HttpResponseBadRequest


class ProtectedErrorTo4xx:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if type(exception) is ProtectedError:
            return HttpResponseBadRequest('["사용중입니다. 세부 혹은 하위 항목들을 먼저 삭제하시기 바랍니다."]')

        return None
