EXE = Main.exe

.PHONY: all
all: $(EXE)

$(EXE): przyklad.cs zad1.dll
	mcs -r:zad1.dll przyklad.cs -out:$(EXE)
		
zad1.dll: zad1.cs
	mcs zad1.cs -target:library -out:zad1.dll
		
.PHONY: run
run:
	mono $(EXE)
		
.PHONY: clean
clean:
	rm $(EXE) zad1.dll
