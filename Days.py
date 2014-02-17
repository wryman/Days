def main(): 
  day = int (input ('Enter day:')) 
  month = int (input ('Enter month:')) 
  year = int (input ('Enter year:')) 
  if month == 1: 
    a = 11 
    year = year - 1 
  if month == 2: 
    a = 12 
    year = year - 1 
  if month == 3: 
    a = 1 
  if month == 4: 
    a = 2 
  if month == 5: 
    a = 3 
  if month == 6: 
    a = 4 
  if month == 7: 
    a = 5 
  if month == 8: 
    a = 6 
  if month == 9: 
    a = 7 
  if month == 10: 
    a = 8 
  if month == 11: 
    a = 9 
  if month == 12: 
    a = 10 
  b = day 
  d = year // 100 
  c = year % 100 
  w = (13 * a - 1) // 5 
  x = c // 4 
  y = d // 4 
  z = w + x + y + b + c - 2 * d 
  r = z % 7 
  r = (r + 7) % 7 
  if r == 0: 
    print ('The day is Sunday') 
  elif r == 1: 
    print ('The day is Monday') 
  elif r == 2: 
    print ('The day is Tuesday') 
  elif r == 3: 
    print ('The day is Wednesday') 
  elif r == 4: 
    print ('The day is Thursday') 
  elif r == 5: 
    print ('The day is Friday') 
  elif r == 6: 
    print ('The day is Saturday') 
  print(a)
  print(b)
  print(c)
  print(d)
main()
