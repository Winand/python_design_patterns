def post_slack_message(channel: str, msg: str) -> None:
    "Send slack message mock."
    print(f"[SlackBot - {channel}]: {msg}")
