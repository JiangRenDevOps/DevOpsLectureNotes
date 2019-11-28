import os
import click
import requests
from pandas import read_csv, DataFrame


@click.command()
@click.option("--in", "-i", "in_file",
              required=True,
              help="Path to csv file to be processed.",
              # type=click.Path(exists=True, dir_okay=False, readable=True)
              )
@click.option("--out", "-o", "out_file",
              default="output.csv",
              help="Path to excel file to store the result.",
              # type=click.Path(dir_okay=False)
              )
@click.option("--dev", "server_url", help="dev server",
              flag_value='http://0.0.0.0:5000',
              default=True
              )
@click.option("--prod", "server_url", help="prod server",
              flag_value='https://real.server.com',
              )
@click.option('--username', prompt=True,
              default=lambda: os.environ.get('USERNAME', ''))
@click.password_option()
@click.option('--verbose', is_flag=True, help="Verbose output")
def process(in_file: str,
            out_file: str,
            server_url: str,
            username: str,
            password: str,
            verbose: bool):
    """ Processes the input file IN and stores the result to
    output file OUT.
    """
    input = read_csv(in_file)
    output = process_csv(input, verbose)
    #output.to_csv(out_file)

    if server_url:
        login_to(server_url, username, password)
        #upload_to(in_file, server_url)


def login_to(server_url: str, username: str, password: str):
    s = requests.Session()
    r = s.post(url=server_url + "/login", data={"username": username, "password": password})
    print(f"This is the session cookie {s.cookies}\n"
          f"This is the session header {s.headers}\n")
    print(f"This is the response status code {r.status_code}\n"
          f"This is the response cookie {r.cookies}\n"
          f"This is the response header {r.headers}\n"
          f"This is the response url {r.url}\n"
          f"This is the response text {r.text}\n")


def upload_to(in_file: str, server_url: str):
    try:
        r = requests.post(url=server_url + "/upload_files", files={'file': open(in_file, 'rb')})
        r.raise_for_status()
    except Exception as e:
        print(f"Error! {e}")
    # if r.status_code != 201:
    #     raise Exception(f"Error! The status code is {r.status_code}")


def process_csv(input: DataFrame, verbose: bool) -> DataFrame:
    # Could you return a subset of the dataframe? From 2019-1 to 2019-4, only Adj Close and Volume columns
    if verbose:
        print("start processing csv")
    return input


if __name__ == "__main__":
    process()
