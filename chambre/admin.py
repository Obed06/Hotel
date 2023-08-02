from django.contrib import admin
from .models import (
	TypeChambre,
	TypeLit,
	Chambre
)




admin.site.register(Chambre)
admin.site.register(TypeChambre)
admin.site.register(TypeLit)

