"""
Does this code run? Does it pass type checking?
Use an enum to improve type safety and detect the problems in this code.
Then, fix the code.
"""

from typing import Any


def send_notification(
    user: dict[str, Any],
    channel: str,
    message: str,
) -> bool:
    match channel:
        case "email":
            print(f'Sending email to {user["email"]}: {message}')
            return True

        case "sms":
            print(f'Sending SMS to {user["phone"]}: {message}')
            return True

        case "push":
            print(f'Sending push notification to {user["device_id"]}: {message}')
            return True


user = {
    "name": "Rodrigo",
    "email": "rodrigo@example.com",
    "phone": "+351912345678",
    "device_id": "device-123",
}

send_notification(user, "email", "Your order has shipped.")
send_notification(user, "sms", "Your login code is 123456.")
send_notification(user, "push", "You have a new message.")
send_notification(user, "webhook", "Something happened.")
