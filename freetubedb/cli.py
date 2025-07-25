import typer


app = typer.Typer()


@app.command()
def convert():
    print("Hello World!")


if __name__ == "__main__":
    app()
