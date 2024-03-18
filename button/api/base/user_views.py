from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated

from api.models import UserMaster
from api.permission import MesPermission
from api.serializers import UserMasterSerializer, UserMasterSelectSerializer
from rest_framework.pagination import PageNumberPagination


class UserMasterViewSet(viewsets.ModelViewSet):

    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSerializer
    permission_classes = [IsAuthenticated, MesPermission]
    http_method_names = ['get', 'post', 'patch', 'delete']     # to remove 'put'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['factory_classification', 'department_position', 'code']
    # search_fields = ['username']

    pagination_class = PageNumberPagination

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserMaster.objects.all()

        qs = UserMaster.objects.filter(enterprise=self.request.user.enterprise, ).all()

        if 'username' in self.request.query_params:
            username = self.request.query_params['username']
            qs = qs.filter(username__contains=username)

        return qs

    def list(self, request, *args, **kwargs):
        return super().list(request, request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, request, *args, **kwargs)


class UserMasterSelectViewSet(viewsets.ModelViewSet):

    queryset = UserMaster.objects.all()
    serializer_class = UserMasterSelectSerializer
    permission_classes = [IsAuthenticated, MesPermission]
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['factory_classification', 'department_position', 'username', 'code']
    search_fields = ['username']

    pagination_class = None

    def get_queryset(self):
        if self.request.user.is_superuser:
            return UserMaster.objects.all()

        return UserMaster.objects.filter(enterprise=self.request.user.enterprise, ).all()