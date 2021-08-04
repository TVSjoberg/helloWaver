from hellowaver import HelloWaver
import click


@click.command()
@click.option('--name', default='Ralph', show_default=True, prompt='What is the name of your friend')
def main(name):
    """ Creates a friendly waver dude. """
    friend = HelloWaver(name)

    click.echo(f"Do you want to wave at {friend.name}?")
    answer = input()
    if answer == 'yes':
        friend.ask_to_wave()
        answer = input('again?')
        if answer == 'yes':
            friend.ask_to_wave()


if __name__ == '__main__':
    main()

