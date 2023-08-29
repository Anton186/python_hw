import argparse
import logging

LOG_FORMAT = '{levelname} - {asctime} - {msg}'

logging.basicConfig(filename='date_checker.log', filemode='a', encoding='utf-8', level=logging.INFO,
                    format=LOG_FORMAT, style='{')
logger = logging.getLogger(__name__)


def if_leap(year: int):
    return not (year % 4 != 0 or year % 100 == 0 and year % 400 != 0)


def check_date(str_date: str) -> bool:
    result = True

    try:
        day, month, year = map(int, str_date.split('.'))
    except ValueError as e:
        logger.error(f'Can\'t parse date sting! Error: {e}')
        raise ValueError(e)

    if not (1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999):
        result = False

    if month in (4, 6, 9, 11) and day > 30:
        result = False

    if month == 2 and if_leap(year) and day > 29:
        result = False

    if month == 2 and not if_leap(year) and day > 28:
        result = False

    logger.info(f'Date: {str_date} - {"" if result else "not "}valid')

    return result


def parse():
    parser = argparse.ArgumentParser(prog='check_date',
                                     description='Checks if input string date valid',
                                     epilog='Date example: 01.01.2000')
    parser.add_argument('-d', '--date', help='Date to check', type=str)
    args = parser.parse_args()
    return check_date(args.date)


if __name__ == '__main__':
    print(parse())