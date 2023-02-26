EXE = Main.exe

.PHONY: all
all: $(EXE)

$(EXE): przyklad.cs zad2.dll
	mcs -r:zad2.dll przyklad.cs -out:$(EXE)
		
zad2.dll: zad2.cs
	mcs zad2.cs -target:library -out:zad2.dll
		
.PHONY: run
run:
	mono $(EXE)
		
.PHONY: clean
clean:
	rm $(EXE) zad1.dll
