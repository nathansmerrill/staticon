colors = {
    'reset': '\033[0m',
    'info': '\033[34m',
    'success': '\033[32m',
    'warning': '\033[93m',
    'error': '\033[91m',
    'critical': '\033[31m'
}

icons = {
    'info': 'i',
    'success': '\u2713',
    'warning': '!',
    'error': 'x',
    'critical': '\u26A0'
}

def message(level, text):
    return f'[{colors[level]}{icons[level]}{colors["reset"]}] {text}'

def sprint(level, text):
    print(message(level, text))
