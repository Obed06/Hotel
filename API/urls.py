from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from django.contrib.auth import views as auth_views

from userprofile.views import (
    inscription_page,
    RegisterView,
    user_list,
    login_view,
    get_email,
    set_staff_and_superuser,
    disable_user,
    get_user_profiles,
    create_user_profile,
)

from chambre.views import (
    get_chambres,
    create_chambre
)

from checkout.views import (
    get_checkout,
    create_checkout
)

from commandeclient.views import (
    get_commandes_clients,
    create_commande_client,
    get_lignes_commande_client,
    create_ligne_commande_client
    
)

from commandefournisseur.views import (
    get_commandes_fournisseurs,
    create_commande_fournisseur,
    get_ligne_commandes_fournisseurs,
    create_ligne_commande_fournisseur
)

from compte.views import (
    get_comptes,
    create_compte
)

from hotel.views import (
    get_hotels,
    create_hotel
)

from inventairecuisine.views import (
    get_inventaire_cuisine,
    create_inventaire_cuisine,
    get_lignes_inventaire_cuisine,
    create_ligne_inventaire_cuisine
)

from inventairemagasin.views import (
    get_inventaire_magasin,
    create_inventaire_magasin,
    get_lignes_inventaire_magasin,
    create_ligne_inventaire_magasin
)

from notification.views import (
    get_notification,
    create_notification
)

from produit.views import (
    get_produits,
    create_produit
)

from reservation.views import (
    get_reservations,
    create_reservation
)

from service.views import (
    get_services,
    create_service
)

from stockcuisine.views import (
    get_stocks_cuisine,
    create_stock_cuisine
)

from stockmagasin.views import (
    get_stocks_magasin,
    create_stock_magasin
)

from transaction.views import (
    get_transactions,
    create_transaction
)


from currency.views import (
    currency_list,
    get_exchange_rate,
    create_exchange_rate
)



urlpatterns = [
    path("admin/", admin.site.urls, name="connect"),
    path('user/login/', login_view, name="login"),
    
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    
    path('inscription/register/', RegisterView.as_view(), name="inscription_register_api"),
    path('api/user/list/', user_list, name='users'),
    path('inscription/', inscription_page, name="inscription"),
    
    path('change/', auth_views.PasswordChangeView.as_view(), name="password_change"),
    path('change/done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    
    path('getEmail/', get_email, name="mail"),
    path('set-staff-superuser/', set_staff_and_superuser, name="set_status"),
    path('disable-user/', disable_user, name="disable-user"),



    path("getu/", get_user_profiles),
    path("createu/", create_user_profile),

    path("getChambre/", get_chambres),
    path("createChambre/", create_chambre),

    path("getCheckout/", get_checkout),
    path("createCheckout/", create_checkout),

    path("getcc/", get_commandes_clients),
    path("createcc/", create_commande_client),
    path("getlcc/", get_lignes_commande_client),
    path("createlcc/", create_ligne_commande_client),

    path("getcf/", get_commandes_fournisseurs),
    path("createcf/", create_commande_fournisseur),
    path("getlcf/", get_ligne_commandes_fournisseurs),
    path("createlcf/", create_ligne_commande_fournisseur),

    path("getCompte/", get_comptes),
    path("createCompte/", create_compte),

    path("geth/", get_hotels),
    path("createh/", create_hotel),

    path("getic/", get_inventaire_cuisine),
    path("createic/", create_inventaire_cuisine),
    path("getlic/", get_lignes_inventaire_cuisine),
    path("createlic/", create_ligne_inventaire_cuisine),

    path("getim/", get_inventaire_magasin),
    path("createim/", create_inventaire_magasin),
    path("getlim/", get_lignes_inventaire_magasin),
    path("createlim/", create_ligne_inventaire_magasin),

    path("getn/", get_notification),
    path("createn/", create_notification),

    path("getp/", get_produits),
    path("createp/", create_produit),

    path("getr/", get_reservations),
    path("creater/", create_reservation),

    path("gets/", get_services),
    path("creates/", create_service),

    path("getsc/", get_stocks_cuisine),
    path("createsc/", create_stock_cuisine),

    path("getsm/", get_stocks_magasin),
    path("createsm/", create_stock_magasin),

    path("gett/", get_transactions),
    path("createt/", create_transaction),

    path("getCurrency/", currency_list),
    path("getRate/", get_exchange_rate),
    path("createRate/", create_exchange_rate),
]



