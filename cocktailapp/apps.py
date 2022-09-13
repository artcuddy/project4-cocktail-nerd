from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cocktailapp'

    # add this
    def ready(self):
        """
        Gets the user signup details
        """
        import cocktailapp.signals # noqa
