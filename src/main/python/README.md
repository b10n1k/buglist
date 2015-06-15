# buglist
buglist has been planned to be used for bugzilla ids tracking in your local machine.

## Requirements
argparse
sqlite3

## Examples
Add a bug number
```bash
bug.py -a 123456
```
or add more
```bash
bug.py -a 123456 77889900
```

Delete bug ids
```bash
bugs.py -r 123456
```

Display a list of ids
```bash
bugs.py -d 
```
