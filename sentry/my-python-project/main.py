import sentry_sdk

sentry_sdk.init(
    dsn="http://df8f938f9c2b89fdb55ec59b840b9aa0@localhost:9100/2",
    send_default_pii=True,
    environment="development",
    release="1.0.0",
)

if __name__ == "__main__":
    sentry_sdk.capture_message("Hello, world")
    #raise Exception("Тестовая ошибка")
    division_zero = 1 / 0
