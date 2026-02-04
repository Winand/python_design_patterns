def send_email(name: str, address: str, subject: str, body: str) -> None:
    "Send email mock."
    print(f"Sending email to {name} ({address})")
    print("==========")
    print(f"Subject {subject}")
    print(body)
