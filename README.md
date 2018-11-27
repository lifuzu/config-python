
# Read json, yaml, toml as config

continue on hcl, ucl, etc.

# Functions:
```
load(fp: object, lang: str = "json") -> dict:
    '''Load a file to dictionary, format should be read from extension;
    unless specified by the second argument `lang`
    '''
```

```
load_str(s: str, lang: str = "json") -> dict:
    ''' Load a string to dictionary, by default, json format
    '''
```

```
load_multifile(fps: list = []) -> dict:
    '''Multiple config files to read,
    format has to be decided by file extension;
    If there is duplicated, overwrite by the following content
    '''
```

```
load_markdown(raw_url: str = '', tag: str = '') -> dict:
    '''Load the config from markdown file,
    with the following format:
    ```json tag="abc"
    {
      "a": "b",
      "c": 10
    }
    ```
    or
    ```toml tag="bcd"
    # This is a TOML document.
    title = "TOML Example"
    [owner]
    name = "Tom Preston-Werner"
    dob = 1979-05-27T07:32:00-08:00 # First class dates
    ```
    or
    ```yaml tag="cde"
    invoice: 34843
    date   : 2001-01-23
    ```
    '''
```
