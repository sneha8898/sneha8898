def expanding(l):
        diff= l[1]-l[0]
        for i in range(2,len(l)):
            if abs(l[i]-l[i-1])>diff:
                diff=abs(l[i]-l[i-1])
            else:
                return False
        return True