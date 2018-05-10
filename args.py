from argparse import ArgumentParser


def create_argument_parser():
    parser = ArgumentParser()

    parser.add_argument('-c', '--child_count', default=2)
    parser.add_argument('-l', '--lower_bound', default=0)
    parser.add_argument('-u', '--upper_bound', default=128)
    parser.add_argument('-v', '--levels', default=5)

    return parser
