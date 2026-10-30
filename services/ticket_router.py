
def route_ticket(subject, message):
    text = f"{subject} {message}".lower()

    # Identify the correct support team
    if any(word in text for word in [
        "payment", "refund", "invoice", "billing", "charged"
    ]):
        category = "Billing"
        team = "Billing Team"
        priority = "High"

    elif any(word in text for word in [
        "login", "error", "bug", "crash", "technical", "password"
    ]):
        category = "Technical Support"
        team = "Technical Support Team"
        priority = "High"

    elif any(word in text for word in [
        "delivery", "shipping", "order status", "tracking"
    ]):
        category = "Order Support"
        team = "Customer Service Team"
        priority = "Medium"

    else:
        category = "General Support"
        team = "General Support Team"
        priority = "Low"

    return {
        "Category": category,
        "Assigned_Team": team,
        "Priority": priority,
        "Status": "Open"
    }


if __name__ == "__main__":
    result = route_ticket(
        "Payment failed",
        "My payment was deducted but my order failed."
    )

    print(result)
