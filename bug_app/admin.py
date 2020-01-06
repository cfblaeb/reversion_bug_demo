from django.contrib import admin
from reversion.admin import VersionAdmin
from .models import MyFirstModel, MySecondModel


@admin.register(MyFirstModel)
class MyFirstModelAdmin(VersionAdmin):
	pass


@admin.register(MySecondModel)
class MySecondModelAdmin(VersionAdmin):
	def reversion_register(self, model, **options):
		options["follow"] = ("alink",)
		super().reversion_register(model, **options)
