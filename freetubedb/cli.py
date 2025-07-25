from typing import Optional
from pathlib import Path
import typer
from typing_extensions import Annotated

from freetubedb.custom_types import Parser, ParserOutput
from freetubedb.constants import YT_FILE_TO_PARSER
from freetubedb.models import Exportable


app = typer.Typer()


@app.command(name="import")
def import_youtube(
    export_file: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
        ),
    ],
):
    parser: Optional[Parser] = YT_FILE_TO_PARSER.get(export_file.name)
    if not parser:
        print(
            f'No parser was found for "{str(export_file)}". Are you sure this is a YouTube export file?'
        )
        raise typer.Exit(code=1)

    output: ParserOutput = parser(export_file)
    if not isinstance(output, Exportable):
        print(
            "[ERROR/DEBUG] output not Exportable!!!"
        )  # TODO: write a propper error message here
        raise typer.Exit(code=1)

    output.export_to_file(Path("./output.db"))
    print("Success!!!")  # TODO: write a propper success message here


if __name__ == "__main__":
    app()
