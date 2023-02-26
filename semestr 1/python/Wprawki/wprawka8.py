def isfree(y, x, wynik):
  if y>=0 and y<n and x>=0 and x<n:
    if wynik[y][x]==-1: return True
  return False

def skoczek(wynik, y, x, kroki, x_ruchy, y_ruchy):
  if kroki == n*n: return True

  for k in range(0, 8):
    nastepny_y = y+y_ruchy[k]
    nastepny_x = x+x_ruchy[k]

    if isfree(nastepny_y, nastepny_x, wynik):
      wynik[nastepny_y][nastepny_x] = kroki
      if skoczek(wynik, nastepny_y, nastepny_x, kroki+1, x_ruchy, y_ruchy): return True
      wynik[nastepny_y][nastepny_x] = -1

  return False

def init():
  wynik = [[-1 for i in range(n)] for j in range(n)]

  y_ruchy = [2, 1, -1, -2, -2, -1, 1, 2]
  x_ruchy = [1, 2, 2, 1, -1, -2, -2, -1]

  wynik[0][0] = 0

  if skoczek(wynik, 0, 0, 1, x_ruchy, y_ruchy):
    for i in range(0, n):
      for j in range(0, n):
        if wynik[i][j] < 10: print(wynik[i][j],end='  ')
        else: print(wynik[i][j],end=' ')
      print()
    return True
  return False

n = 6
print(init())