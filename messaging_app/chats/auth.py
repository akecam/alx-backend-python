from rest_framework import authentication


class ReadOrWriteOnly(authentication.TokenAuthentication):

    def authenticate(self, request):
        return super().authenticate(request)