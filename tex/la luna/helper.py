from lunarcalendar import Converter, Solar, Lunar, DateNotExist

YEAR = 2025
MONTH_LENGTH = [31, 28 + int(YEAR%4 == 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def moon_str(month, day):
    output = '         '
    if day <= MONTH_LENGTH[month-1]:
        lunar_day = Converter.Solar2Lunar(Solar(YEAR, month, day)).day
        output = '\moon{'
        output += str(lunar_day)
        output += '}'
    return output

def print_row(day):
    row = '  {\Large ' + str(day) + '} & '
    for month in range(1, 12):
        row += moon_str(month, day) + ' & '
    row += moon_str(12, day) + ' \\\\'
    print(row)

if __name__ == '__main__':
    for day in range(1, 32):
        print_row(day)