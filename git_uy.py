def lik_raqamlar(n:int, nom:str):
    f1=open('new.txt','r')
    count=0
    print(f'({n}) lik {nom} RAQAMLAR:')
    print()
    new=f'({n})'
    for i in f1.read().split('\n'):
        if i[4:8]==new:
            count+=1
            if count==15:
                break
            else:
                print(i)
    f1.close()

def yanami(n:int, nom:str):
            yana=int(input(' Yanami: [1]HAA   [0]YOQ: '))
            print()
            count1=0
            f1=open('new.txt','r')
            new=f'({n})'
            if yana==1:
                print(f'({n})lik {nom} RAQAMLAR:')
                print()
                for i in f1.read().split('\n'):
                    if i[4:8]==new:
                        count1+=1
                        if count1==20:
                            break
                        else:
                            print(i)
            f1.close()
            tanla=input('Raqam tanlang: ')
            yes_no=int(input('Rostdan ham shu raqamni sotib olmoqchimisiz: [1]HA   [0]YOq: '))
            if yes_no==1:
                print('Xaridingiz uchun raxmat!!!')
                with open('soldNumbers.txt','a') as nums:
                    nums.write(f'{tanla}\n')
            if yana==0:
                
                tanla=input('Raqam tanlang: ')
                yes_no=int(input('Rostdan ham shu raqamni sotib olmoqchimisiz: [1]HA   [0]YOq: '))
                if yes_no==1:
                    print('Xaridingiz uchun raxmat!!!')
                    with open('soldNumbers.txt','a') as nums:
                        nums.write(f'{tanla}\n')
def yana(n:int,a:int,b:int):
                yana=int(input(' Yanami: [1]HAA   [0]YOQ: '))
                print()
                count1=0
                f1=open('new.txt','r')
                if yana==1:
                  print(f'{n} lik RAQAMLAR:')
                  print()
                  for i in f1.read().split('\n'):
                    if i[a:b]==t:
                        count1+=1
                        if count1==20:
                            break
                        else:
                            print(i)
                f1.close()
                tanla=input('Raqam tanlang: ')
                yes_no=int(input('Rostdan ham shu raqamni sotib olmoqchimisiz: [1]HA   [0]YOq: '))
                if yes_no==1:
                    print('Xaridingiz uchun raxmat!!!')
                    with open('soldNumbers.txt','a') as nums:
                        nums.write(f'{tanla}\n')
                
                if yana==0:
                  tanla=input('Raqam tanlang: ')
                  yes_no=int(input('Rostdan ham shu raqamni sotib olmoqchimisiz: [1]HA   [0]YOq: '))
                  if yes_no==1:
                    print('Xaridingiz uchun raxmat!!!')
                    with open('soldNumbers.txt','a') as nums:
                        nums.write(f'{tanla}\n')

def raqamlar(n,a:int,b:int):
    f1=open('new.txt','r')
    count=0
    print(f'({n}) lik RAQAMLAR:')
    print()
    for i in f1.read().split('\n'):
    
        if i[a:b]==n:
            count+=1
            if count==15:
                break
            else:
                print(i)
    f1.close()
    

print()
n=int(input('''[1]Kompaniya boyicha qidirish   
[2]Qolip boyicha qidirish: 
'''))
print()
if n==1:
    n1=int(input('''[1]Beeline
[2]Uzmobile
[3]MobiUz
[4]Humans
'''))
    print()
    if n1==1:
        n2=int(input('''[1] (90)-
[2] (91)-
'''))
        if n2==1:
            lik_raqamlar(90, 'BEELINE')

            yanami(90,'BEELINE')

        elif n2==2:
            lik_raqamlar(91,'BEELINE')
            

            yanami(91,'BEELINE')
 
    elif n1==2:
        n3=int(input('''[1] (95)-
[2] (99)-
'''))
        if n3==1:
            lik_raqamlar(95, 'UzMobile')

            yanami(95,'UzMobile')
        elif n3==2:
            lik_raqamlar(99,'UzMobile')
            
            yanami(99,'UzMobile')
        
    elif n1==3:
        n4=int(input('''[1] (97)-
[2] (96)-
'''))
        if n4==1:
            lik_raqamlar(97, 'MobiUz')

            yanami(97,'MobiUz')
        elif n4==2:
            lik_raqamlar(96, 'MobiUz')
            yanami(96, 'MobiUz')
        
    elif n1==4:
        n5=int(input('''[1] (92)-
[2] (94)-
'''))
        if n5==1:
            lik_raqamlar(92, 'Humans')

            yanami(92,'Humans')
        elif n5==2:
            lik_raqamlar(94,'Humans')
            yanami(94, 'Humans')
elif n==2:
    tanla=input('XX(kodi) XXX XX XX:  ')
    lst=[]
    for t in tanla.split():
        lst.append(t)
        if t.isdigit():
            ind_t=lst.index(t)
            if ind_t==0:

                raqamlar(t,5,7)
                yana(t,5,7)

            elif ind_t==1:

                raqamlar(t,9,12)
                yana(t,9,12)
            elif ind_t==2:

                raqamlar(t,13,15)
                yana(t,13,15)

            elif ind_t==3:

                raqamlar(t,15,18)
                yana(t,15,18)
print()
