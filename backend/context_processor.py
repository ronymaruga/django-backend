import datetime

def current_year(request):
    """
    Context processor to add the current year to the context.
    This can be used in templates to display the current year dynamically.
    """
    return {
        'current_year': datetime.datetime.now().year
    }