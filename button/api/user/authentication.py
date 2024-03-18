# from datetime import timedelta
# from django.conf import settings
# from django.utils.timezone import now
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.exceptions import AuthenticationFailed
#
# #
# def get_expire_time():
#     return now() - timedelta(seconds=settings.AUTH_TOKEN_EXPIRE_SECONDS)
#
#
# class ExpiredTokenCheck(TokenAuthentication):
#     def authenticate(self, request):
#         return super().authenticate(request)
#
#     def authenticate_credentials(self, key):
#         model = self.get_model()
#         try:
#             token = model.objects.get(key=key)
#         except model.DoesNotExist:
#             raise AuthenticationFailed('로그인 정보가 유효하지 않습니다.')
#
#         if not token.user.is_active:
#             raise AuthenticationFailed('인증된 사용자가 아닙니다.')
#
#         if token.created < get_expire_time():
#             raise AuthenticationFailed('로그인정보가 만료되었습니다. 다시 로그인해주세요')
#
#         return token.user, token
