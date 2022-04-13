from ast import arg
import asyncio
import sys
import pathlib

from checker.checker import site_is_online, site_is_online_async
from checker.cli import read_user_cli_args, display_check_results

def _get_websites_urls(args):
    urls = args.urls
    if args.input_file:
        urls += _read_urls_from_file(args.input_file)
    return urls


def _read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: empty input file, {file}", file=sys.stderr)
    else:
        print("Error: input file not found", file=sys.stderr)
    return []

def _synchronous_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_results(result, url, error)

async def _asynchronous_check(urls):
        async def _check(url):
            error = ""
            try:
                result = await site_is_online_async(url)
            except Exception as e:
                result = False
                error = str(e)
            display_check_results(result, url, error)
        await asyncio.gather(*[_check(url) for url in urls])


def main():
    args = read_user_cli_args()
    urls = _get_websites_urls(args)
    if not urls:
        print("Error: no URLs to check", file=sys.stderr)
        sys.exit(1)
    if args.asynchronous:
        asyncio.run(_asynchronous_check(urls))
    else:
        _synchronous_check(urls)

if __name__ == "__main__":
    main()