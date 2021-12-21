import typer

from datetime import datetime
from pathlib import Path
from workalendar.usa import Kansas
from yaml import dump

try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper


def main():
    kansas = Kansas()
    this_year = datetime.now().year

    for year in range(this_year, this_year + 3):
        path = Path("_data", f"calendar-{year}.yml")
        events = {"events": list()}
        holidays = kansas.holidays(year)
        for holiday in holidays:
            events["events"].append(
                {"title": str(holiday[1]), "start_date": holiday[0]}
            )

        path.write_text(dump(events, Dumper=Dumper))


if __name__ == "__main__":
    typer.run(main)
