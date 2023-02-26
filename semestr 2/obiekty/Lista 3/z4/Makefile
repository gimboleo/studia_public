EXE = Main.exe

.PHONY: all
all: $(EXE)

$(EXE): przyklad.cs zad4.dll
	mcs -r:zad4.dll przyklad.cs -out:$(EXE)
		
zad4.dll: zad4.cs
	mcs zad4.cs -target:library -out:zad4.dll
		
.PHONY: run
run:
	mono $(EXE)
		
.PHONY: clean
clean:
	rm $(EXE) zad4.dll
