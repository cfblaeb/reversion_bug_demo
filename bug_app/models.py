from django.db import models


class MyFirstModel(models.Model):
	astring = models.TextField()


class MySecondModel(models.Model):
	alink = models.ForeignKey(MyFirstModel, on_delete=models.PROTECT)
