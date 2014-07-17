from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS

from score import CheckioRefereePep8

MAX_LINES = 12
MAX_LINE_LENGTH = 80


def inspector(code, runner=None):
    lines = code.split("\n")
    if len(lines) > MAX_LINES:
        return False, "Your code should have no more than 12 lines"
    if any(len(line.replace("\t", "    ")) > MAX_LINE_LENGTH for line in lines):
        return False, "Each line should be no more than 80 symbols."
    return True, None


api.add_listener(
    ON_CONNECT,
    CheckioRefereePep8(
        tests=TESTS,
        inspector=inspector,
        function_name="twist"
    ).on_ready)
