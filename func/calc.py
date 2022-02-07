

# 1 + 2 = 3
# 1 + 'a' ==> 预期结果 报错， None

def add(a, b):
    """当a, b 都不是数字的时候，返回 None"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    return None
    # logger
    # 相加出现问题
    # logger.warning()


def minus(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b


def multiply(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b


def division(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b !=0 :
        return a / b
