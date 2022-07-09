def draw_stars(n):
  if n==1:
    return ['*']

  S=draw_stars(n//3)
  L=[]

  for i in S:
    L.append(i*3)
  for i in S:
    L.append(i+' '*(n//3)+i)
  for i in S:
    L.append(i*3)

  return L

N=int(input())
print('\n'.join(draw_stars(N)))