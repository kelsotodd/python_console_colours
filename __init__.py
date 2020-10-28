import os

os.system("")

# Group of Different functions for different styles
colours = [
    ('BLACK','\033[30m'),
    ('RED', '\033[31m'),
    ('GREEN','\033[32m'),
    ('YELLOW','\033[33m'),
    ('BLUE','\033[34m'),
    ('MAGENTA','\033[35m'),
    ('CYAN','\033[36m'),
    ('WHITE','\033[37m'),
    ('UNDERLINE','\033[4m'),
    ('RESET', '\033[0m')
]

for colour in colours:
    print(colour[1] + "Hello, World!")


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()