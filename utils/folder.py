import os

def multi_makedirs(*args):
    """为给定的多个路径创建目录, 如果路径不存在, 则创建它"""
    for path in args:
        if not os.path.exists(path):
            os.makedirs(path)