import io
import time
import requests


def _get(command:str, arg1:str, arg2:str = "", arg3:str = "") -> str:
    BASE_URL = "https://rest.kegg.jp"
    delay = 0.3333333333 # third of a second
    url = f"{BASE_URL}/{command}/{arg1}/{arg2}/{arg3}"

    response = requests.get(url)
    time.sleep(delay)
    return response.text


def kegg_conv(target_db: str, source_db: str, option: str = ""):
    """Convert KEGG identifiers to/from outside identifiers.

    Args:
        target_db (str): Target database for conversion
        source_db (str): Source database or database entries (can be a single entry or multiple entries joined by '+')
        option (str, optional): Output format. Can be "turtle" or "n-triple". Defaults to None.

    Returns:
        TextIOWrapper: File-like object containing the conversion results

    Raises:
        ValueError: If invalid option is provided or if arguments are missing/invalid
    """
    if option and option not in ["turtle", "n-triple"]:
        msg = "Invalid option arg for kegg conv request."
        raise ValueError(msg)

    if isinstance(source_db, list):
        source_db = "+".join(source_db)

    if target_db and source_db != ("" or None):
        return _get("conv", target_db, source_db, option) if option else _get("conv", target_db, source_db)

    else:
        msg = "Bad argument target_db or source_db for kegg conv request."
        raise ValueError(msg)
