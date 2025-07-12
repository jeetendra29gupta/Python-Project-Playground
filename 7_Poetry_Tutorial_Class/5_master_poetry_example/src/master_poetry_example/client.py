import click


@click.command()
@click.option("--name", default="World", help="Name to greet")
def main(name: str):
    print(f"Hello, {name} from Click + Poetry!")
