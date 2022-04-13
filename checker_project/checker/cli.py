import argparse

def read_user_cli_args():
    """Handle the CLI arguments and options"""
    parser = argparse.ArgumentParser(description="Check if a site is up and running")
    parser.add_argument("-u",
     "--urls",
     metavar="URLs",
     nargs="+",
     type=str,
     default=[],
     help="enter one or mor website Urls")

    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )

    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="run the connectivity check asynchronously",
    )
    
    return parser.parse_args()

def display_check_results(result, url, error=""):
    """Display the results of the check"""
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Error: "{error}"')
        