# python_practice
Practice ThreadPoolExecutor

```
➜  python_practice git:(main) ✗ python3 main.py -h             
usage: main.py [-h] --max_workers MAX_WORKERS

Practice ThreadPoolExecutor

optional arguments:
  -h, --help            show this help message and exit
  --max_workers MAX_WORKERS

```
```
➜  python_practice git:(main) ✗ python3 main.py --max_workers 2
start 2021-08-08 15:32:16.647665
doing job1 0
doing job1 1
doing job2 0
doing job2 1
doing job1 2
doing job1 3
doing job2 2
doing job2 3
doing job1 4
doing job1 5
doing job2 4
doing job2 5
doing job1 6
doing job1 7
doing job2 6
doing job2 7
doing job1 8
doing job1 9
doing job2 8
doing job2 9
end 2021-08-08 15:32:21.681038
execution time 0:00:05.033373

```