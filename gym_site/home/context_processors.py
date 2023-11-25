from home.models import Setting


def setting(request):
    return {'setting': Setting.objects.all(pk=1)}