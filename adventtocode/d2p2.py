from typing import List
from d2p1 import get_d2_input

def is_report_safe_with_dampener(report: List[int], counter:int = 0)->int:
    if len(report) < 2:
        return True
    def inrange(curr, _next):
        _diff = -1 if curr < _next else 1
        return _diff * (curr - _next) in range(1,4)
    for (ind,rep_lev), rep_sans_first_lev in zip(enumerate(report[:-1]), report[1:]):
        if not inrange(rep_lev, rep_sans_first_lev):
            if counter == 0:
                counter += 1
                try:
                    if ind + 2 > len(report) - 1:
                        print('I am true by default of len : ' , report)
                        return True
                    if ind > 1:
                        if inrange(report[ind - 1], rep_sans_first_lev):
                            new_report = report[:ind] + report[ind + 1 : ]
                        else:
                            new_report = report[:ind + 1] + report[ind + 2 :]
                    elif ind == 1 :
                        if inrange(report[ind - 1], rep_sans_first_lev):
                            new_report = report[:ind] + report[ind + 1 : ]
                        else:
                            new_report = report[ind: ]
                    else:
                        if inrange(rep_lev, report[ind + 2]):
                            new_report = [rep_lev] + report[ind + 2:]
                            print("I'm here")
                        else:
                            print("i am not here")
                            new_report = report[ind + 1:]
                        
                    
                    print('counting...', ind, new_report)
                    return is_report_safe_with_dampener(new_report,counter)
                except Exception as e:
                    print('exception: ',e)
            else:
                return False
    print('I am true without pause : ', report)
    return True

def main():
    safe_reports_count = sum(is_report_safe_with_dampener(report) for report in get_d2_input())
    print(safe_reports_count)
if __name__ == "__main__":
    main()