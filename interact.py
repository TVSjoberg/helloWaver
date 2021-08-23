from typing import DefaultDict
from hellowaver import HelloWaver
import click


@click.command()
@click.option('--name', default='Ralph', show_default=True, prompt='What is the name of your friend')
def main(name):
    """ Creates a friendly waver dude. """
    friend = HelloWaver(name)
    still_interacting = True

    while still_interacting:

        want_to_wave = click.confirm(f"Do you want to wave at {friend.name}?", default=None)
        if want_to_wave:
            friend.ask_to_wave()
        else:
            still_interacting = not click.confirm(f"Do you want to leave?", default=True)

    if friend.has_waved:
        click.echo(f'{friend.name} is all puckered out from all that waving')
    else:
        click.echo(f'{friend.name} looks sad as you leave')

if __name__ == '__main__':
    main()
