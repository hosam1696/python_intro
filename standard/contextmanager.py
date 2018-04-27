class LoggingContextManager:
    def __enter__(self):
        print('Logginf context Manager __enter')
        return 'You are in a with statement'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Logging context Manager __exit {}, {}, {}'.format(exc_type, exc_val, exc_tb))
        pass