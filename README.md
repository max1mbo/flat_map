# Coding Challenge

## flat_map

```
./flat_json.py --help
usage: flat_json.py [-h] [--test] [filename]

positional arguments:
  filename    input filename, default: stdin

optional arguments:
  -h, --help  show this help message and exit
  --test      run tests
```

## tests

```
./flat_json.py --test
...
```

## stdin

```
cat test.json | ./flat_json.py 
{
 "a": "a", 
 "c.c.test": true, 
 "b": "c", 
 "c.c.verbose": false, 
 "c.c.clob": "blah blah blah"
}
```

## file

```
./flat_json.py test.json 
{
 "a": "a", 
 "c.c.test": true, 
 "b": "c", 
 "c.c.verbose": false, 
 "c.c.clob": "blah blah blah"
}
```

