
# Utilities
from datetime import datetime
from django.shortcuts import render
from myApp import views as app_views


def index(request):
    """
    Función vista para la página inicio del sitio.
    """

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'tarifas/main.html', {'tarifas' : app_views.getTarifas()}
    )

