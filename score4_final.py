

def pinakas(y):
#y einai col, x einai to tablo tou paixnidiou 
    x=[' ' for i in range(8*y+1)]
    return x
    

    
def pl(x,y):
#y einai col, x einai to tablo tou paixnidiou 
    n=0
    m=0
    b=[' a |',' b |',' c |',' d |',' e |',' f |',' g |',' h |']
     
    if y==5:
        print('','','','','','1','','','2','','','3','','','4','','','5')
        print('','-','-','-','-','-','-','-','-','-','-','-','-') 
        while m<=7*y+1:
            print (b[n],x[m],'|',x[m+1],'|',x[m+2],'|',x[m+3],'|',x[m+4],'|')
            m+=y
            n+=1
        print('','-','-','-','-','-','-','-','-','-','-','-','-')    
    elif y==6:
        print('','','','','','1','','','2','','','3','','','4','','','5','','','6')
        print('','-','-','-','-','-','-','-','-','-','-','-','-','-','-')
        while m<=7*y+1:
            print (b[n],x[m],'|',x[m+1],'|',x[m+2],'|',x[m+3],'|',x[m+4],'|',x[m+5],'|')
            m+=y
            n+=1
        print('','-','-','-','-','-','-','-','-','-','-','-','-','-','-')    
    elif y==7:
        print('','','','','','1','','','2','','','3','','','4','','','5','','','6','','','7')
        print('','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')
        while m<=7*y+1:
            print (b[n],x[m],'|',x[m+1],'|',x[m+2],'|',x[m+3],'|',x[m+4],'|',x[m+5],'|',x[m+6],'|')
            m+=y
            n+=1
        print('','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')    
    elif y==8:
        print('','','','','','1','','','2','','','3','','','4','','','5','','','6','','','7','','','8')
        print('','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')
        while m<=7*y+1:
            print (b[n],x[m],'|',x[m+1],'|',x[m+2],'|',x[m+3],'|',x[m+4],'|',x[m+5],'|',x[m+6],'|',x[m+7],'|')
            m+=y
            n+=1
        print('','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')    
    elif y==9:
        print('','','','','','1','','','2','','','3','','','4','','','5','','','6','','','7','','','8','','','9')
        print('','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')
        while m<=7*y+1:
            print (b[n],x[m],'|',x[m+1],'|',x[m+2],'|',x[m+3],'|',x[m+4],'|',x[m+5],'|',x[m+6],'|',x[m+7],'|',x[m+8],'|')
            m+=y
            n+=1
        print('','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')    
    elif y==10:
        print('','','','','','1','','','2','','','3','','','4','','','5','','','6','','','7','','','8','','','9','','','10')
        print('','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')
        while m<=7*y+1:
            print (b[n],x[m],'|',x[m+1],'|',x[m+2],'|',x[m+3],'|',x[m+4],'|',x[m+5],'|',x[m+6],'|',x[m+7],'|',x[m+8],'|',x[m+9],'|')
            m+=y
            n+=1
        print('','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-')
            
       
    
def available(c,z,x,y,fs=0):
#y einai col,c einai h sthlh pou epilegei o paikths,x einai to tablo tou paixnidiou kai z einai to symvolo tou ekastote paixth(x h' o)
#fs einai oi gemates theseis ths sthlhs pou epilegei o paixths,nc einai h kainourgia sthlh pou epilegei o paixths 
        c+=7*y-1
        if x[c]!='o' and x[c]!='x':
            x[c]=z
            return pl(x,y)
        else:
            if fs!=8:
                fs+=1
                return available(c-(8*y-1),z,x,y,fs=fs)
            else:
                nc=int(input("give another column: "))
                return available(nc,z,x,y,fs=0)



        
def winner(w,pin):
#w einai col,no(o,oo) einai oi fores pou den brethike 4ada,pin einai to tablo tou paixnidiou
    def ori(y=w):
        f=False
        no=0
        i=0
        while i<=len(pin)-4:
            if pin[i]==pin[i+1]==pin[i+2]==pin[i+3] and pin[i]!=' ':
                pin[i]='*'
                pin[i+1]='*'
                pin[i+2]='*'
                pin[i+3]='*'
                f=True
                break
            if no!=y-3 :
                no+=1
            if no!=y-3:
                i+=1
            else:
                no=0
                i+=y-1
        return f==True
        
    def kath(y=w):
        g=False
        i=3*y
        while i<=len(pin)-1:
            if pin[i]==pin[i-y]==pin[i-2*y]==pin[i-3*y] and pin[i]!=' ':
                pin[i]='*'
                pin[i-y]='*'
                pin[i-2*y]='*'
                pin[i-3*y]='*'
                g=True
                break
            else:
                i+=1
        return g==True
            
    def diag(y=w):
        h=False
        z=False
        noo=0
        nooo=0
        i=0
        j=y-2
        while i<=5*y-4: 
            if pin[i]==pin[i+y+1]==pin[i+2*(y+1)]==pin[i+3*(y+1)] and pin[i]!=' ' :
                pin[i]='*'
                pin[i+y+1]='*'
                pin[i+2*(y+1)]='*'
                pin[i+3*(y+1)]='*'
                h=True
                break
            if noo!=y-3:
                noo+=1
            if noo!=y-3:
                i+=1
            else:
                noo=0
                i+=y-1
        if h!=True:
            while j<=5*y-1:
                if pin[j]==pin[j+y-1]==pin[j+2*(y-1)]==pin[j+3*(y-1)] and pin[j]!=' ' :
                    pin[j]='*'
                    pin[j+y-1]='*'
                    pin[j+2*(y-1)]='*'
                    pin[j+3*(y-1)]='*'
                    z=True
                    break
                if nooo!=y-3:
                    nooo+=1
                if nooo==y-3:
                    j+=1
                else:
                    j+=y-1
        return h==True or z==True
    if ori(y=w)==True or kath(y=w)==True or diag(y=w)==True:
        return True
    else:
        return False
        
        


def game_on(col,pinak):
    m=[' ' for i in range (len(pinak))]
    pl(pinak,col)    
    print('Παίχτη 1 είναι η σειρά σου')
    i=0
    s=False
    cont=' '
    while s==False and cont!='s':
        while winner(col,pinak)!=True and i<=len(pinak):
            if i%2==0 and i>1 :
                cont=input('Πατήστε οποιοδήποτε πλήκτρο για να συνεχίσετε.\nΓια παύση του παιχνιδιού και αποθήκευση σε αρχείο επιλέξτε "s":')
            if i>=1: 
                if cont!='s':
                    print('Παίχτη', i%2+1 ,'είναι η σειρά σου')
            if cont!='s':
                k=int(input("Επίλεξε στήλη για το πιόνι σου: "))
            while k<=0 or k>col:
                k=int(input("Επίλεξε διαφορετική στήλη για το πιόνι σου: "))
            if i%2==0:
                r='x'
            else:
                r='o'
            if i>=1 and cont=='s':
                sg=input('Δώστε όνομα αρχείου:')
                for c in range (len(pinak)):
                    if pinak[c]=='o':
                        m[c]=1
                    elif pinak[c]=='x':
                        m[c]=2
                    elif pinak[c]==' ':
                        m[c]=0
                mm=m
                with open(f'{sg}.csv','w',newline='') as f:
                    writer=csv.writer(f,delimiter=',')
                    writer.writerow(mm)
                print('Το παιχνίδι αποθηκεύτηκε')
                break
            else:
                available(k,r,pinak,col,fs=0)
            if winner(col,pinak)!=True:
                i+=1
        if cont!='s':
            print('Ο παίχτης',i%2+1,'σχημάτισε τετράδα')
            pl(a,col)
            l=input("Θέλετε να ξαναπαίξετε;: ")
            if  l=='ναι' or l=='NAI' or l=='Ναι' or l=='ΝΑΙ' or l=='nai' or l=='Nai':
                pinak=pinakas(col)
                pl(pinak,col)
                print('Παίχτη 1 είναι η σειρά σου')
                i=0
            elif l=='οχι' or l=='όχι' or l=='ΌΧΙ' or l=='ΟΧΙ' or l=='Όχι' or l=='Οχι' or l=='oxi' or l=='OXI' or l=='Oxi':
                s=True
                print('Τα λέμε αργότερα')
    
import csv    
print('Καλωσορίσατε στο παιχνίδι!')
game=input("Επιθυμείτε νέο παιχνίδι (ΝG) ή φόρτωση παιχνιδιού από αρχείο (S);")
while game!='NG' and game!='S':
    print("Μη έγκυρος χαρακτήρας. Δοκιμάστε ξανά :")
    game=input("Επιθυμείτε νέο παιχνίδι (ΝG) ή φόρτωση παιχνιδιού από αρχείο (S);")
if game=='NG':
    col=int(input("Δώστε αριθμό στυλών: "))
    while col<5 or col>10:
        col=int(input("Δώστε διαφορετικό αριθμό στυλών: "))
    a=pinakas(col)
    game_on(col,a)
else:
    sg=input('Όνομα αποθηκευμένου παιχνιδιού: ')
    with open (f'{sg}.csv','r') as f:
        reader=csv.reader(f)
        mm=list(reader)
        col=len(mm[0])//8
        a=pinakas(col)
    for i in range (col*8):
        if mm[0][i]=='0':
            a[i]=' '
        elif mm[0][i]=='1':
            a[i]='o'
        elif mm[0][i]=='2':
            a[i]='x'
    game_on(col,a)
    
        
        