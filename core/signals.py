from django.dispatch import receiver


@receiver(signal)
def my_signal_receiver(args, **kwargs):
    pass
