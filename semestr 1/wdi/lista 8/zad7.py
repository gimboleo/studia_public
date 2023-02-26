def hanoi(krazki,lewy,srodkowy,prawy):
    if krazki == 1:
        print('Krazek 1 z',lewy,'do',prawy)
        return
    hanoi(krazki-1,lewy,prawy,srodkowy)
    print("Krazek",krazki,'z',lewy,'do',prawy)
    hanoi(krazki-1,srodkowy,lewy,prawy)

hanoi(5,'a','b','c')