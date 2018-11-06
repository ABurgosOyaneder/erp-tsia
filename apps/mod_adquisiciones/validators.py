from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Aqui van las validaciones

def ValidateMayorCero(value):

    if value == 0:
        raise ValidationError(_("El valor no puede ser 0"))
    else:
        return value
