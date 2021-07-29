import string
import random
from django.utils.text import slugify


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_folio_generator(instance):
    """
    Este es para un proyecto de Django y se asume que la instancia
    tiene un modelo con un campo de Folio (Slugfield)
    """
    new_folio = random_string_generator()

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(folio=new_folio).exists()
    if qs_exists:
        return unique_folio_generator(instance)
    return new_folio