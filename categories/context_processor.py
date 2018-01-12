from .models import Category

def get_categories(request):
    categories_names = Category.objects.filter(is_active=True)
    return locals()