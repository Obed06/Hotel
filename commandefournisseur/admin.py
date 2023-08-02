from django.contrib import admin
from .models import (
	CommandeFournisseur,
	LigneCommandeFournisseur
)




admin.site.register(CommandeFournisseur)
admin.site.register(LigneCommandeFournisseur)

