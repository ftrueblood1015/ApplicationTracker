from django.contrib import admin
from django.apps import apps
from django.conf import settings


# Register your models here.
class ListAdminMixin(object):
    def __init__(self, admin_model, admin_site):
        self.list_display = [field.name for field in admin_model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


models = apps.get_models()
for model in models:
    admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
    try:
        admin.site.register(model, admin_class)
    except admin.sites.AlreadyRegistered:
        pass
