import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread, current_thread
import logging

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")
args = vars(parser.parse_args())
source = Path(args.get("source"))
output = Path(args.get("output"))


def scroll_folder(path: Path) -> None:
    logging.info(f"Start process {current_thread().name} in {path}")
    for el in path.iterdir():
        if el.is_dir():
            inner_process = Thread(target=scroll_folder, args=(el,))
            inner_process.start()
        else:
            copy_file(el)


def copy_file(path: Path) -> None:
    ext = path.suffix[1:]
    ext_folder = output / ext
    try:
        ext_folder.mkdir(exist_ok=True, parents=True)
        copyfile(path, ext_folder / path.name)
    except OSError as err:
        logging.error(err)


if __name__ == "__main__":
    pr = Thread(target=scroll_folder, args=(source,))
    pr.start()
    pr.join()
    print(f'Вміст папки {source} було відсортовано в папку {output}')
