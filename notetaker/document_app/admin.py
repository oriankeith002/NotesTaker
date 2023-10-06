from django.contrib import admin
from .models import Document # importing our model here
# Register your models here.

admin.site.register(Document) # use the database models we just created