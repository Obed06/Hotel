from django.contrib import admin
from .models import (
	CommandeClient,
	LigneCommandeClient
)




admin.site.register(CommandeClient)
admin.site.register(LigneCommandeClient)

