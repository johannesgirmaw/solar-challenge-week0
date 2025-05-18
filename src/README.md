## Run the main.py script

```
python src/main.py
```

Incasing running issues like this

```
Traceback (most recent call last):
  File "/home/<username>/10Academy/Week0/code/solar-challenge-week1/src/main.py", line 1, in <module>
    from scripts.read_file import read_csv_file
ModuleNotFoundError: No module named 'scripts'
```

Run this command

It will add the project root explicitly to PYTHONPATH

```
cd solar-challenge-week1
export PYTHONPATH=$PYTHONPATH:$(pwd)
```
