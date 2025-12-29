import warnings
from django.test.runner import DiscoverRunner
from django.test.utils import override_settings
from django.conf import settings


class CustomTestRunner(DiscoverRunner):
    def __init__(self, *args, **kwargs):
        kwargs["timing"] = True  # force timing always on
        kwargs["shuffle"] = True  # force shuffling always on
        kwargs["verbose"] = 2  # force verbosity to 2 always
        kwargs["durations"] = 0  # show 10 slowest tests
        super().__init__(*args, **kwargs)

    def setup_test_environment(self, **kwargs):
        super().setup_test_environment(**kwargs)
        settings.DEBUG = False  # override here
        print(">>> Running tests with DEBUG=False")

    def run_tests(self, *args, **kwargs):
        # Show all warnings once, especially to show DeprecationWarning
        # messages which Python ignores by default
        warnings.simplefilter("always")
        with override_settings(**TEST_SETTINGS):
            return super().run_tests(*args, **kwargs)


TEST_SETTINGS = {
    "EMAIL_BACKEND": "django.core.mail.backends.console.EmailBackend",
    "PASSWORD_HASHERS": ["django.contrib.auth.hashers.MD5PasswordHasher"],
}
