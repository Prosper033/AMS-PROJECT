def prompt_for_valid_integer_input(prompt: str) -> int:
    return int(prompt_for_valid_input(prompt, __check_for_valid_integer))


def prompt_for_non_empty_string(prompt: str) -> str:
    return prompt_for_valid_input(prompt, __check_non_empty_string)


def prompt_for_valid_input(prompt: str, check):
    while True:
        entry = input(prompt)
        if check(entry):
            break
    return entry


def __check_for_valid_integer(obj):
    try:
        int(obj)
        return True
    except ValueError:
        return False


def __check_non_empty_string(obj):
    return len(str(obj).strip()) != 0
