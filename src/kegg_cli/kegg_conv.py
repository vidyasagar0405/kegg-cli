import io
import time
from urllib.request import urlopen

from Bio._utils import function_with_previous


@function_with_previous
def _q(op, arg1, arg2=None, arg3=None):
    delay = 0.333333333  # one third of a second
    current = time.time()
    wait = _q.previous + delay - current
    if wait > 0:
        time.sleep(wait)
        _q.previous = current + wait
    else:
        _q.previous = current

    URL = "https://rest.kegg.jp/%s"
    if arg2 and arg3:
        args = f"{op}/{arg1}/{arg2}/{arg3}"
    elif arg2:
        args = f"{op}/{arg1}/{arg2}"
    else:
        args = f"{op}/{arg1}"
    resp = urlopen(URL % (args))

    if arg2 == "image":
        return resp

    handle = io.TextIOWrapper(resp, encoding="UTF-8")
    handle.url = resp.url
    return handle


_q.previous = 0


def kegg_conv(target_db, source_db, option=None):
    """KEGG conv - convert KEGG identifiers to/from outside identifiers.

    Arguments:
     - target_db - Target database
     - source_db_or_dbentries - source database or database entries
     - option - Can be "turtle" or "n-triple" (string).

    """
    if option and option not in ["turtle", "n-triple"]:
        msg = "Invalid option arg for kegg conv request."
        raise ValueError(msg)

    if isinstance(source_db, list):
        source_db = "+".join(source_db)

    if target_db and source_db != ("" or None):
        return _q("conv", target_db, source_db, option) if option else _q("conv", target_db, source_db)

    else:
        msg = "Bad argument target_db or source_db for kegg conv request."
        raise ValueError(msg)
