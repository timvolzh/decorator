import datetime


def log_decorator_with_path(path_to_logs):
    def log_decorator(function_for_logging):
        def logger(*args, **kwargs):
            start_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
            func_name = function_for_logging.__name__
            arguments = str(args)[1:-1] + str(kwargs)[1:-1]
            result = function_for_logging(*args, **kwargs)
            with open(path_to_logs, "w", encoding='utf-8') as f:
                f.write(f'Start time: {start_time}\nFunction name: {func_name}\nArguments: {arguments}')
            return result
        return logger
    return log_decorator

