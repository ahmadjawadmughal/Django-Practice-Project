from django.core.signals import request_finished, request_started
from django.db.models.signals import post_save
from .views import signup
from django.contrib.auth.models import User
from django.dispatch import receiver, Signal


def callback_function(sender, **kwargs):
    print("request started!")

request_started.connect(callback_function)    



@receiver(post_save, sender=User)
def success(sender, **kwargs):
    print("User is created successfuly!")

# post_save.connect(success, sender=User)


"""Custom signal"""


pizza_done = Signal() #signal define


class PizzaStore:

    def send_pizza(self, topping, size):
        pizza_done.send(sender=self.__class__, topping= topping, size=size) #signal send


# reciever

@receiver(pizza_done)
def notify_kitchen(sender, **kwargs): #signal reciever
    print("You're pizza is ready:", kwargs)


obj = PizzaStore()
obj.send_pizza("special topping", "family")

