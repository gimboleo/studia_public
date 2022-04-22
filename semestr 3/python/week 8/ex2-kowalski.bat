@echo off
IF EXIST "bootleg_imdb.db" DEL "bootleg_imdb.db"

python ex2-kowalski.py Directors --add John Doe
python ex2-kowalski.py Directors --add Jakub Kowalski
python ex2-kowalski.py Directors --add No One

python ex2-kowalski.py Producers --add Jane Smith
python ex2-kowalski.py Producers --add Jan Nowak

python ex2-kowalski.py Movies --add "Ghost Movie" 666 None None
python ex2-kowalski.py Movies --add "Sample Movie" 2021 1 1
python ex2-kowalski.py Movies --add "Polish Movie" 2020 2 2
python ex2-kowalski.py Movies --add "Sample Polish Movie" 2019 1 2

python ex2-kowalski.py Movies --show
echo( & echo( & echo(
python ex2-kowalski.py Directors --show
echo( & echo( & echo(
python ex2-kowalski.py Producers --show