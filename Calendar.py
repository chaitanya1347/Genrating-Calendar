def leapyear(n):
    if n % 4 != 0:
        return "False"
    elif n % 100 != 0:
        return "True"
    elif n % 400 != 0:
        return "False"
    else:
        return "True"

def jan_first(n, i):
        r = 1753

        while (r != n):
            if leapyear(r) == "True":
                if i + 2 > 6:
                    if i == 5:
                        i = 0
                        r = r + 1
                    else:
                        i = 1
                        r = r + 1
                else:
                    i = i + 2
                    r = r + 1
            elif leapyear(n) == "True" and r==n-1:
                if i + 2 > 6:
                    if i == 5:
                        i = 0
                        r = r + 1
                    else:
                        i = 1
                        r = r + 1
                else:
                    i = i + 2
                    r = r + 1
            else:

                   if i + 1 > 6:
                     i = 0
                     r = r + 1
                   else:
                     i = i + 1
                     r = r + 1
        return i

def first(n,i):
    r = 1753
    while (r != n):
        if leapyear(r) == "True":
            if i + 2 > 6:
                if i == 5:
                    i=0
                    r = r + 1
                else:
                    i=1
                    r=r+1
            else:
                i = i + 2
                r = r + 1
        else:
            if i+1>6:
                i=0
                r=r+1
            else:
             i = i + 1
             r = r + 1
    return i

def initiation1(n,m):
  l=[first(n,0),first(n,3),jan_first(n,3),jan_first(n,6),jan_first(n,1),jan_first(n,4),jan_first(n,6),jan_first(n,2),jan_first(n,5),jan_first(n,0),jan_first(n,3),jan_first(n,5)]
  if l[m]==0:
   s='1'
   for i in range(2, 8 - l[m]):

      s += '  ' + str(i)
  else:
    s = ' ' * (3*l[m]-2)
    for i in range(1,8-l[m]):

          s += '  ' + str(i)

  return ' '+ s


def initiation2( start, end):
    if start >end:
        s=''
    else:
     if start<=9 :
       s=' '+ str(start)
     elif start>30:
        s='  '
     else:
        s=str(start)
     for i in range(start+1, end + 1):
        if i <= 9:
            s += '  ' + str(i)

        elif i > 30:

            s += '   '
        else:
            s += ' ' + str(i)
    return s

def initiation3( start, end):
  if start > end:
        s = ''
  else:
    if start<=9:
       s=' '+ str(start)
    elif start>31:
        s='  '
    else:
        s=str(start)
    for i in range(start+1, end + 1):
        if i <= 9:
            s += '  ' + str(i)
        elif i>31:
            s+='   '
        else:
            s += ' ' + str(i)
    return s

def initiation4( n,start, end):
   if leapyear(n)=="True":

     if start > 29:
        s = '   '

     else:
        s = str(start)
     for i in range(start + 1, end + 1):
            if i > 29:
                s += '   '
            else:
                s += ' ' + str(i)
   else:
       if start > 28:
           s = '  '

       else:
           s = str(start)
       for i in range(start + 1, end + 1):
         if i > 28:
            s += '   '
         else:
            s += ' ' + str(i)
   return s


def row1(n,t):
    a = "M"
    b = "T"
    c = "W"
    d = "T"
    e = "F"
    f = "S"
    g = "S"
    l = [first(n, 0), first(n, 3), jan_first(n, 3), jan_first(n, 6), jan_first(n, 1), jan_first(n, 4), jan_first(n, 6),         jan_first(n, 2), jan_first(n, 5), jan_first(n, 0), jan_first(n, 3), jan_first(n, 5)]
    r = '       {}  {}  {}  {}  {} \n {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}'.format(        'JANUARY', ' ' * 18, 'FEBRUARY', ' ' * 16, 'MARCH', a, b, c, d, e, f, g, ' ' * 4, a, b, c, d, e, f, g, ' ' * 4,a, b, c, d, e, f, g)
    start1 = 8 - l[0]
    end1 = 6 + start1
    start2 = 8 - l[1]
    end2 = 6 + start2
    start3 = 8 - l[2]
    end3 = 6 + start3
    print(r,file=t)
    print(initiation1(n, 0) + ' ' * 7 + initiation1(n, 1) + ' ' * 7 + initiation1(n, 2),file=t)
    print(initiation2(start1, end1) + ' ' * 7 + initiation2(start2, end2) + ' ' * 7 + initiation2(start3, end3),file=t)
    print(initiation2(end1 + 1, end1 + 7) + ' ' * 7 + initiation2(end2 + 1, end2 + 7) + ' ' * 7 + initiation2(end3 + 1, end3 + 7),file=t)
    print( initiation2(end1 + 8, end1 + 14) + ' ' * 7 + initiation2(end2 + 8, end2 + 14) + ' ' * 7 + initiation2(end3 + 8, end3 + 14),file=t)
    if leapyear(n) == 'False':
        print(initiation3(end1 + 15, end1+21) + ' ' * 7 + initiation4(n,end2 + 15, end2+21) + ' ' * 7+ initiation3(end3 + 15, end3+21),file=t)
    else:
        print(initiation3(end1 + 15, end1+21) + ' ' * 7 + initiation4(n,end2 + 15, end2+21) + ' ' * 7 + initiation3(end3 + 15, end3+21),file=t)
    print(initiation3(end1 +22, end1+28) + ' ' * 33 + initiation3(end3 + 22, end3+28),file=t)

def row2(n,t):
    a = "M"
    b = "T"
    c = "W"
    d = "T"
    e = "F"
    f = "S"
    g = "S"
    l = [first(n, 0), first(n, 3), jan_first(n, 3), jan_first(n, 6), jan_first(n, 1), jan_first(n, 4), jan_first(n, 6),         jan_first(n, 2), jan_first(n, 5), jan_first(n, 0), jan_first(n, 3), jan_first(n, 5)]
    r = '{}  {}  {}  {}  {}  {} \n {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}'.format(' '*7,'APRIL', ' ' * 19, 'MAY', ' ' * 19, 'JUNE', a, b, c, d, e, f, g, ' ' * 4, a, b, c, d, e, f, g, ' ' * 4,a, b, c, d, e, f, g)
    start1 = 8 - l[3]
    end1 = 6 + start1
    start2 = 8 - l[4]
    end2 = 6 + start2
    start3 = 8 - l[5]
    end3 = 6 + start3
    print(r,file=t)
    print(initiation1(n, 3) + ' ' * 7 + initiation1(n, 4) + ' ' * 7 + initiation1(n, 5),file=t)
    print(initiation2(start1, end1) + ' ' * 7 + initiation2(start2, end2) + ' ' * 7 + initiation2(start3, end3),file=t)
    print(initiation2(end1 + 1, end1 + 7) + ' ' * 7 + initiation2(end2 + 1, end2 + 7) + ' ' * 7 + initiation2(end3 + 1, end3 + 7),file=t)
    print( initiation2(end1 + 8, end1 + 14) + ' ' * 7 + initiation2(end2 + 8, end2 + 14) + ' ' * 7 + initiation2(end3 + 8, end3 + 14),file=t)
    print(initiation2(end1 + 15, end1 +21) + ' ' * 7 + initiation3(end2 + 15, end2+21) + ' ' * 7 + initiation2(end3 + 15, end3+21),file=t)
    print(initiation2(end1 + 22, end1+28) + ' ' * 7 + initiation3(end2 + 22, end2 + 28) + ' ' * 7 + initiation2(end3 + 22, end3 + 28),file=t)

def row3(n,t):
    a = "M"
    b = "T"
    c = "W"
    d = "T"
    e = "F"
    f = "S"
    g = "S"
    l = [first(n, 0), first(n, 3), jan_first(n, 3), jan_first(n, 6), jan_first(n, 1), jan_first(n, 4), jan_first(n, 6),         jan_first(n, 2), jan_first(n, 5), jan_first(n, 0), jan_first(n, 3), jan_first(n, 5)]
    r = '       {}  {}  {}  {}  {} \n {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}'.format(        'JULY', ' ' * 20, 'AUGUST', ' ' * 16, 'SEPTEMBER', a, b, c, d, e, f, g, ' ' * 4, a, b, c, d, e, f, g, ' ' * 4,a, b, c, d, e, f, g)
    start1 = 8 - l[6]
    end1 = 6 + start1
    start2 = 8 - l[7]
    end2 = 6 + start2
    start3 = 8 - l[8]
    end3 = 6 + start3
    print(r,file=t)

    print(initiation1(n, 6) + ' ' * 7 + initiation1(n, 7) + ' ' * 7 + initiation1(n, 8),file=t)
    print(initiation2(start1, end1) + ' ' * 7 + initiation2(start2, end2) + ' ' * 7 + initiation2(start3, end3),file=t)
    print(initiation2(end1 + 1, end1 + 7) + ' ' * 7 + initiation2(end2 + 1, end2 + 7) + ' ' * 7 + initiation2(end3 + 1, end3 + 7),file=t)
    print( initiation2(end1 + 8, end1 + 14) + ' ' * 7 + initiation2(end2 + 8, end2 + 14) + ' ' * 7 + initiation2(end3 + 8, end3 + 14),file=t)
    print(initiation3(end1 + 15, end1 +21) + ' ' * 7 + initiation3(end2 + 15, end2+21) + ' ' * 7 + initiation2(end3 + 15, end3+21),file=t)
    print(initiation3(end1 + 22, end1+28) + ' ' * 7 + initiation3(end2 + 22, end2 + 28) + ' ' * 7 + initiation2(end3 + 22, end3 + 28),file=t)


def row4(n,t):
    a = "M"
    b = "T"
    c = "W"
    d = "T"
    e = "F"
    f = "S"
    g = "S"
    l = [first(n, 0), first(n, 3), jan_first(n, 3), jan_first(n, 6), jan_first(n, 1), jan_first(n, 4), jan_first(n, 6),
         jan_first(n, 2), jan_first(n, 5), jan_first(n, 0), jan_first(n, 3), jan_first(n, 5)]
    r = '       {}  {}  {}  {}  {} \n {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}'.format( 'OCTOBER', ' ' * 16, 'NOVEMBER', ' ' * 15, 'DECEMBER', a, b, c, d, e, f, g, ' ' * 4, a, b, c, d, e, f, g, ' ' * 4, a, b, c,   d, e, f, g)
    start1 = 8 - l[9]
    end1 = 6 + start1
    start2 = 8 - l[10]
    end2 = 6 + start2
    start3 = 8 - l[11]
    end3 = 6 + start3
    print(r,file=t)

    print(initiation1(n, 9) + ' ' * 7 + initiation1(n, 10) + ' ' * 7 + initiation1(n, 11),file=t)
    print(initiation2(start1, end1) + ' ' * 7 + initiation2(start2, end2) + ' ' * 7 + initiation2(start3, end3),file=t)
    print(initiation2(end1 + 1, end1 + 7) + ' ' * 7 + initiation2(end2 + 1, end2 + 7) + ' ' * 7 + initiation2(end3 + 1,end3 + 7),file=t)
    print(initiation2(end1 + 8, end1 + 14) + ' ' * 7 + initiation2(end2 + 8, end2 + 14) + ' ' * 7 + initiation2(end3 + 8,end3 + 14),file=t)
    print(initiation3(end1 + 15, end1 + 21) + ' ' * 7 + initiation2(end2 + 15, end2 + 21) + ' ' * 7 + initiation3(end3 + 15, end3 + 21),file=t)
    print(initiation3(end1 + 22, end1 + 28) + ' ' * 7 + initiation2(end2 + 22, end2 + 28) + ' ' * 7 + initiation3(end3 + 22, end3 + 28),file=t)
    return ""

def calendar(n,t):
  print('='*34,n,'='*34,'\n',file=t)
  row1(n,t)
  print('-' * 74, file=t)
  row2(n,t)
  print('-' * 74, file=t)
  row3(n,t)
  print('-' * 74, file=t)
  row4(n,t)
  print('='*74,file=t)



t=open('CALENDAR.txt','w')
n=2022
calendar(n,t)
t.close()