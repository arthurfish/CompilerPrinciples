import re


def expression_transform(expression: str) -> list:
    def priority(op: str) -> int:
        if op == '#':
            return -1
        if op == '(':
            return 0
        elif op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
    def is_operator(op: str) -> bool:
        return op in ['+', '-', '*', '/']

    def top(lst: list) -> any:
        if len(lst) != 0:
            return lst[-1]
        else:
            return '#'


    S1 = []
    S2 = []
    index = 0
    while index < len(expression):
        character = expression[index]
        if character.isdigit():
            value = 0
            while expression[index].isdigit():
                value = value * 10 + int(expression[index])
                index += 1
            S2.append(str(value))
            continue
        elif is_operator(character):
            if priority(character) > priority(top(S1)):
                S1.append(character)
            else:
                while True:
                    S2.append(S1.pop())
                    if priority(top(S1)) < priority(character):
                        break
                S1.append(character)
        elif character == '(':
            S1.append(character)
        elif character == ')':
            while top(S1) != '(':
                S2.append(S1.pop())
            S1.pop()
        elif character == '#':
            while len(S1) != 0:
                S2.append(S1.pop())
        index += 1

    return S2

def test_expression_transformer():
    print(expression_transform("1+2+34#"))

test_expression_transformer()

def regular_expression_practice():
    def filename_validator(filename: str) -> bool:
        return re.fullmatch(r'\w+\.(?=jpg|jpeg|gif|bmp)', filename) is not None

    def datetime_validator(datetime_str: str) -> bool:
        m = re.fullmatch(r'(\d+)/(\d+)/(\d+)', datetime_str)
        if len(m.groups()) != 3:
            return False
        month, day, year = m.groups()
        month, day, year = int(month), int(day), int(year)
        if  (1 <= month <= 12) and (1 <= day <= 31) and (0 <= year):
            return True
        else:
            return False

    def phone_number_validator(phone_number: str) -> (bool, str):
        m = re.fullmatch(r'\((\d{4})\)\d{8}-\d{4}', phone_number)
        if m is None:
            return False, -1
        return True, m.group(0)

    def extract_all_hyperlinks(content: str) -> list[str]:
        result = re.findall(r'(?=\")http\w+(?=\")', content)
        return result

    def extract_title_and_content(input_string: str) -> tuple[str, str]:
        pass