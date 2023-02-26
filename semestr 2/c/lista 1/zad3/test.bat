@ECHO OFF
gcc -o zad3 zad3.c
.\zad3.exe < wejscie.txt > wyjscie.txt
more wejscie.txt
@ECHO:
more wyjscie.txt
PAUSE