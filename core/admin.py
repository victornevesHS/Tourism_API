from django.contrib import admin
from .models import PontoTuristico
from .models import DocIdentificacao

admin.site.register(DocIdentificacao)
admin.site.register(PontoTuristico)