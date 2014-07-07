from checkio.referees.io import CheckiOReferee
from checkio import api

import pep8_157 as pep8
import sys


def count_pep8(code):
    pep8style = pep8.StyleGuide(parse_argv=False, config_file=False, max_line_length=79)
    options = pep8style.options
    sys.stdout = None
    raw_lines = code.splitlines()
    lines = [l + "\n" for l in raw_lines[:-1]] + raw_lines[-1:]
    checker = pep8.Checker(lines=lines, options=options)
    checker.check_all()
    report = checker.report
    sys.stdout = sys.__stdout__

    result = []
    score = 0


    for line_number, offset, error_code, text, doc in report._deferred_print:
        result.append([line_number, offset, error_code, text])
        if error_code.startswith("E"):
            score += 2
        elif error_code.startswith("W"):
            score += 1
    return score, result


class CheckioRefereePep8(CheckiOReferee):
    def check_current_test(self, data):
        if self.inspector:
            inspector_result, inspector_result_addon = self.inspector(self.code, self.runner)
            self.inspector = None
            self.current_test["inspector_result_addon"] = inspector_result_addon
            if not inspector_result:
                self.current_test["inspector_fail"] = True
                api.request_write_ext(self.current_test)
                return api.fail(0, inspector_result_addon)
        user_result = data['result']

        check_result = self.check_user_answer(user_result)
        self.current_test["result"], self.current_test["result_addon"] = check_result

        api.request_write_ext(self.current_test)

        if not self.current_test["result"]:
            return api.fail(self.current_step, self.get_current_test_fullname())

        if self.next_step():
            self.test_current_step()
        else:
            if self.next_env():
                self.restart_env()
            else:
                score, pep8_results = count_pep8(self.code)
                api.request_write_in("FINAL", "req")
                api.request_write_ext({"result": True, "check_data": pep8_results})
                api.success(score)
