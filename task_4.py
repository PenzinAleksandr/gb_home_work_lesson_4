import sys
import util


if __name__ == "__main__":

    args = sys.argv[1:]

    for code in args:
        conv = util.currency_rates(code)
        if conv:
            cur, date = conv
            date = date.strftime("%d-%m-%Y")
            print(f"{cur}, {date}")
