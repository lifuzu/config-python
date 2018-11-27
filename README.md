README.md

json, yaml, toml as conf
hcl, ucl, etc.

load: load from a file handler
load_str: load a string to dict

```
# specify string with markdown style, such as
# ```json
# {
#   "a": "b",
#   "c": 10
# }
# ```
# or
# ```toml
# # This is a TOML document.
# title = "TOML Example"
# [owner]
# name = "Tom Preston-Werner"
# dob = 1979-05-27T07:32:00-08:00 # First class dates
# ```
# or
# ```yaml
# invoice: 34843
# date   : 2001-01-23
# ```
#
```