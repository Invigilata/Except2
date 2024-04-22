class InvalidDataException(Exception):
    pass

class ProcessingException(Exception):
    pass

def generate_exception(case):
    if case == 1:
        raise InvalidDataException("InvalidDataException.")
    elif case == 2:
        raise ProcessingException("Processing exception")
    else:
        raise Exception("Unknown exception")

def main_function(case):
    try:
        generate_exception(case)
    except InvalidDataException as e:
        print(f"Обнаружено InvalidDataException: {e}")
        raise
    except ProcessingException as e:
        print(f"Обнаружено ProcessingException: {e}")
        raise
    except Exception as e:
        print(f"Обнаружено неизвестное исключение: {e}")
        raise

try:
    main_function(1)
except InvalidDataException as e:
    print(f"Обнаружено InvalidDataException в main: {e}")
except ProcessingException as e:
    print(f"Обнаружено ProcessingException в main: {e}")
except Exception as e:
    print(f"Обнаружено неизвестное исключение в main: {e}")