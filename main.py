datne = open('txt/admin.txt')
print('===Lasa datni===', datne.name )
for rinda in datne:
  print (rinda, end= '')
datne.close()
print('\n')
datne = open('txt/viesis.txt')
print('===Lasa datni===', datne.name )
for rinda in datne:
  print (rinda, end= '')
datne.close()
print('\n')
datne = open('txt/admin.txt')
sum = 0
i=0
for rinda in datne:
  dati = rinda.split(' ')
  sum += int(dati[3])
  i=i+1
print('admin_vid_vecums = ', sum/i)
print('\n')
print('adminu daudzums', i)
vecums = 0
for rinda in datne:
  dati = rinda.split(' ')
  vecums = int(dati[3])
#max_vecums = max(vecums)
#print('admin max age: ', max_vecums)  
#min_vecums = min(vecums)
#print('admin min age: ', min_vecums)
print('\n')
datne = open('txt/viesis.txt')
j=0
for rinda in datne:
  dati = rinda.split(' ')
  j=j+1
print('viesu daudzums', j)