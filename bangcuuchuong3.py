def bangcuuchuong(n,i=1):
    if i > 10:
        return
    print(n,'x',i,'=',n*i,end='\t| ')
    bangcuuchuong(n,i+1)

def tatcabangcuuchuong(n=1):
    if n>10:
        return
    bangcuuchuong(n)
    print()
    tatcabangcuuchuong(n + 1)

tatcabangcuuchuong()