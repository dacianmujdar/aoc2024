
def is_report_safe(report):
    if report == sorted(report) or report == sorted(report, reverse=True):
        diff = [abs(report[i] - report[i + 1]) for i in range(len(report) - 1)]
        if min(diff) >= 1 and max(diff) <= 3:
            return True
    return False


if __name__ == '__main__':
    with open("./input/day2.txt", "r") as f:
        lines = f.readlines()

    response = 0
    for line in lines:
        report = [int(nr) for nr in line.split(" ")]
        if is_report_safe(report):
            response += 1
            continue
        for i in range(len(report)):
            if is_report_safe(report[0:i] + report[i+1:]):
                response += 1
                break

    print(response)