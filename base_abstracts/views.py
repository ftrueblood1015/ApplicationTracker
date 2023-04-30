from django.shortcuts import render
from rest_flex_fields import FlexFieldsModelViewSet


# Create your views here.
class FlexFieldsTrackingModel(FlexFieldsModelViewSet):
    def create(self, request, *args, **kwargs):
        if request.data:
            request.data['creator'] = request.user.id
            request.data['last_updater'] = request.user.id
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.data:
            request.data['last_updater'] = request.user.id
        return super().update(request, *args, **kwargs)
