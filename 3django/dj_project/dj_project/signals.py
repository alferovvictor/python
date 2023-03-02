from django.dispatch import receiver
import django.dispatch

my_sygnal = django.dispatch.Signal()

@receiver(my_sygnal)
def my_callback(sender, **kwargs):
    print(f"the signal time is: {kwargs.get('now')}")
