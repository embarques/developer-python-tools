import click
import sys

@click.command()
@click.option("--name", default="world")
def main(name: str):
    click.echo(f"Hello, {name} (from Click)")
    click.echo(f"Python used: {sys.executable}")

if __name__ == "__main__":
    main()
