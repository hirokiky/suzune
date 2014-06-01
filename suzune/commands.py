import argparse
import webbrowser

from suzune import db as suzune_db


def get(opt):
    url = suzune_db.get(opt.tag)
    if url:
        print(url)
        webbrowser.open(url)
    else:
        print('Image Url does not exist')


def tags(opt):
    print('List of tags:')
    print('\n'.join(['{tag} ({num})'.format(tag=tag, num=num) for tag, num in suzune_db.tags()]))


def add(opt):
    suzune_db.add(opt.url[0], opt.tags)
    print('Added the url')


def build_parser():
    parser = argparse.ArgumentParser(description="Suzune: a command line image registration tool.")
    subparsers = parser.add_subparsers()

    subcommand = subparsers.add_parser('get', help="Getting a image by specifying tag name")
    subcommand.add_argument('tag', type=str, help="Tag name of images you want to get")
    subcommand.set_defaults(func=get)

    subcommand = subparsers.add_parser('tags', help="A list of tags")
    subcommand.set_defaults(func=tags)

    subcommand = subparsers.add_parser('add', help="Adding a image for suzune's db")
    subcommand.add_argument('url', type=str, nargs=1, help="Image url")
    subcommand.add_argument('tags', type=str, nargs='+', help="Tags for adding image url")
    subcommand.set_defaults(func=add)
    return parser


def run():
    parser = build_parser()
    opt = parser.parse_args()

    if hasattr(opt, 'func'):
        suzune_db.init_db()
        opt.func(opt)
    else:
        parser.print_help()
