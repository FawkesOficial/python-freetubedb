from typing import Optional
from pathlib import Path
import typer
from typing_extensions import Annotated

from freetubedb.custom_types import Parser, ParserOutput
from freetubedb.constants import YT_FILE_TO_PARSER, YT_TO_FREETUBE_FILENAME
from freetubedb.models import Exportable


app = typer.Typer()


@app.command(name="import")
def import_youtube(
    export_file: Annotated[
        Path,
        typer.Argument(
            help="A YouTube export file (ex: search-history.json, watch-history.json, etc)",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
            resolve_path=True,
        ),
    ],
    output_path: Annotated[
        Optional[Path],
        typer.Option(
            "--output",
            "-o",
            help="The output path (FreeTube correspondent db file by default)",
            writable=True,
            resolve_path=True,
        ),
    ] = None,
):
    parser: Optional[Parser] = YT_FILE_TO_PARSER.get(export_file.name)
    if not parser:
        print(
            f'[ERROR] No parser was found for "{export_file.name}". '
            "Are you sure this is a supported YouTube export file?"
        )
        raise typer.Exit(code=1)

    output: ParserOutput = parser(export_file)
    if not isinstance(output, Exportable):
        print(
            f"[ERROR] Parsed output from {export_file.name} is not exportable. "
            "Ensure the parser returns an object implementing `Exportable`."
        )
        raise typer.Exit(code=1)

    default_filename: str = YT_TO_FREETUBE_FILENAME[export_file.name]
    if output_path and output_path.is_dir():
        output_path = output_path.joinpath(default_filename)
    else:
        output_path = Path(".").joinpath(default_filename)

    output_path.write_text(output.export() + "\n")

    print(
        f"[SUCCESS] YouTube export from '{export_file.name}' imported and written to '{output_path.resolve()}'"
    )


if __name__ == "__main__":
    app()
