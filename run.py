"""
Usage:
    cli login <username> <password>
    cli signin <username> <password>
    cli (-i | --interactive)
    cli (-h | --help)
    cli -q | --quit
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys, os
import cmd

from app.views import Cli
from docopt import docopt, DocoptExit

'''
Application instance
'''
app = Cli()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def helper_fn(self, arg):
        try:
            opt = docopt(helper_fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    helper_fn.__name__ = func.__name__
    helper_fn.__doc__ = func.__doc__
    helper_fn.__dict__.update(func.__dict__)
    return helper_fn

opt = docopt(__doc__, sys.argv[1:])
arguments = docopt(__doc__)

class MyInteractive (cmd.Cmd):

    intro = " WELCOME TO ANDELA KENYA "

    prompt = ' >>> '
    file = None

    @docopt_cmd
    def help(self, args):
        """usage: help [<command>]"""
        print(opt)

    @docopt_cmd
    def login(self,args):

        """Usage: create_room <room_type> <room_name>...
        """

        app.login(args['<username>'], args['<password>'] )

    @docopt_cmd
    def signup(self, args):

        """Usage: add_person <first_name> <second_name> <person_type> [ <wants_accommodation> ]
        """

        app.signup(args['<username>'], args['<password>'])

    @docopt_cmd
    def add_comments(self, args):

        """Usage: add_person <first_name> <second_name> <person_type> [ <wants_accommodation> ]
        """

        app.add_comments(args['<username>'], args['<password>'])
            

    @docopt_cmd
    def do_quit(self, args):
        """usage: quit"""
        print('Good Bye!')
        exit()



if opt['--interactive']:
    MyInteractive().cmdloop()

if opt['--help']:
    print(opt)

print(opt)