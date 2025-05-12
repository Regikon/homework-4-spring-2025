import re

class RegExpUrl(object):

    def __init__(self, url_pattern: str) -> None:
        self.__expr = re.compile(url_pattern)
        self.__url_pattern = url_pattern

    @property
    def url_pattern(self):
        return self.__url_pattern

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, RegExpUrl):
            return self.__expr == value.__expr
        if isinstance(value, str):
            result = self.__expr.match(value)
            return result is not None
        return False

