import logging
from django.cors.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validation_email

logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id,customer_email,customer_name = None):
    try:
        validate_email(customer_email)
        subject = f"Order Confitmation - Order #{order_id}"
        message = f"""
        Hello {customer_name if customer_name else "Customer"},
        Thank you for your Order!
        Your order with ID #{order_id} has been Successfully placed.
        We will notify you once your order is processed
        Best Regards, 
        Customer Support Team
        """

        send_mail(
            subject = subject,
            massage = message,
            from_email = settings.DEFAULT_FROM_EMAIL,
            recipient_list = [customer_email],
            fail_silently = False
        )
        return {
            "status":"success",
            "message":"Order confirmation email sent successfully."
        }
    except ValidationError:
        logger.error(f"Invalid email address provided:{customer_email}")
        return{
            "status":"error",
            "message":"Invalid email address."
        }
    except Exception as e:
        logger.error(f"Error Sending email for order {order_id}:{str(e)}")
        return {
            "status":"error",
            "message":"Failed to send confirmation email."
        }

