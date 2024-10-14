import argparse


def scrypt():
    parser = argparse.ArgumentParser()

    parser.add_argument('number', metavar='N', type=float, nargs=1, help='Вещественное число')
    parser.add_argument('str', metavar='S', type=str, nargs=1, help='Строка')
    parser.add_argument('--verbose', action='store_true', help='Вывод дополнительной информации')
    parser.add_argument('--repeat', type=int, default=1, help='Повторение строки')

    args = parser.parse_args()

    if args.verbose:
        print(f'Полученные аргументы: number = {args.number}, str = {args.str}, repeat = {args.repeat}')

    for i in range(args.repeat):
        print(f'Число = {args.number}, Текст = {args.str}')


if __name__ == '__main__':
    scrypt()
