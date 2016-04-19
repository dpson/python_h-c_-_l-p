import csv
with open('386mb_tovictim1.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dau_vao = (row['Time'])
        i= len(row['Time'])
        delta=0.000009
        false = 0
        d_dos_ra=[]
        a=0
        while a+1 < i:
               if (dau_vao[a+1] - dau_vao[a]) > 0.000009:
                   if false < 1:
                       false +=1
                       a += 1
                   else:
                       d_dos_ra = []
                       continue
               else:
                   
                   if dau_vao[a] in d_dos_ra:
                       d_dos_ra.append[dau_vao[a+1]]
                   else:
                       d_dos_ra.append[dau_vao[a]]
                       d_dos_ra.append[dau_vao[a+1]]
                   a +=1
        print(d_dos_ra)
                     
