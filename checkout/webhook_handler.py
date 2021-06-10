from django.http import HttpResponse


class StripeWH_Handler:
    """
    Webhook to handle Stripe. Code from CI Stripe lesson
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handles an unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handles the payment success webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handles the payment failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
