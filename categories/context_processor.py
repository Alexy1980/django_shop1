from .models import Category

def get_categories(request):
    categories_names = Category.objects.filter(is_active=True)
    return locals()

def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }