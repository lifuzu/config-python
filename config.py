
# `box` let dict with advanced dot notation access.
from box import Box
import importlib
import json
import sys

def load(fp: object, lang: str = "json") -> dict:
    '''Load a file to dictionary, format should be read from extension;
    unless specified by the second argument `lang`
    '''
    mod = importlib.import_module(lang)
    return Box(mod.load(fp))

def load_str(s: str, lang: str = "json") -> dict:
    ''' Load a string to dictionary, by default, json format
    '''
    mod = importlib.import_module(lang)
    if hasattr(mod, "loads"):
        return Box(mod.loads(s))
    elif hasattr(mod, "load"):
        return Box(mod.load(s))
    return None

if __name__ == "__main__":
    str_ = """{
      "a": "b",
      "c": 10
    } """
    print(load_str(str_))
    print(load_str(str_).a)

    str_ = """
      invoice: 34843
      date   : 2001-01-23
    """
    print(load_str(str_, "yaml"))

    str_ = """
      # This is a TOML document.

      title = "TOML Example"

      [owner]
      name = "Tom Preston-Werner"
      dob = 1979-05-27T07:32:00-08:00 # First class dates

      [database]
      server = "192.168.1.1"
      ports = [ 8001, 8001, 8002 ]
      connection_max = 5000
      enabled = true

      [servers]

        # Indentation (tabs and/or spaces) is allowed but not required
        [servers.alpha]
        ip = "10.0.0.1"
        dc = "eqdc10"

        [servers.beta]
        ip = "10.0.0.2"
        dc = "eqdc10"

      [clients]
      data = [ ["gamma", "delta"], [1, 2] ]

      # Line breaks are OK when inside arrays
      hosts = [
        "alpha",
        "omega"
      ]
    """
    print(load_str(str_, "toml"))

    with open("tests/samples/a.json", "r") as fp:
        content = load_str(fp.read(), "json")
        print(content)
        print(content.c)

    with open("tests/samples/b.yaml", "r") as fp:
        content = load(fp, "yaml")
        print(content)
        print(content.date)

    with open("tests/samples/c.toml", "r") as fp:
        content = load(fp, "toml")
        print(content)
        print(content.clients)