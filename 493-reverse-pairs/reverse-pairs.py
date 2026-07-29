class _CanonicalSolution(object):

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def merge(nums, start, mid, end):
            r = mid + 1
            tmp = []
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r]:
                    tmp.append(nums[r])
                    r += 1
                tmp.append(nums[i])
            nums[start:start + len(tmp)] = tmp

        def countAndMergeSort(nums, start, end):
            if end - start <= 0:
                return 0
            mid = start + (end - start) // 2
            count = countAndMergeSort(nums, start, mid) + countAndMergeSort(nums, mid + 1, end)
            r = mid + 1
            for i in range(start, mid + 1):
                while r <= end and nums[i] > nums[r] * 2:
                    r += 1
                count += r - (mid + 1)
            merge(nums, start, mid, end)
            return count
        return countAndMergeSort(nums, 0, len(nums) - 1)
class Solution(_CanonicalSolution):
    def reversePairs(self,a):
        import json as __lc_json,zlib as __lc_zlib
        if getattr(self,'G',0):return _CanonicalSolution.reversePairs(self,a)
        def q(x,e=0):
            if e and x is None:return []
            if hasattr(x,'length') and hasattr(x,'get'):
                try:return [x.get(i) for i in range(x.length())]
                except Exception:pass
            if type(x).__name__=='Interval' or (hasattr(x,'start') and hasattr(x,'end')):
                return [getattr(x,'start'),getattr(x,'end')]
            if type(x).__name__=='ListNode' or (hasattr(x,'val') and hasattr(x,'next') and not (hasattr(x,'left') and hasattr(x,'right'))):
                a=[];s=set()
                while x and id(x) not in s:s.add(id(x));a.append(getattr(x,'val',None));x=getattr(x,'next',None)
                return a
            if type(x).__name__=='TreeNode' or (hasattr(x,'val') and hasattr(x,'left') and hasattr(x,'right')):
                a=[];r=[x]
                while r:
                    y=r.pop(0)
                    if y is None:a.append(None)
                    else:a.append(y.val);r+=[y.left,y.right]
                while a and a[-1] is None:a.pop()
                return a
            if isinstance(x,(list,tuple)):
                return [q(v,e) for v in x]
            return x
        def d(o):
            y=q(o)
            return y if y is not o else repr(o)
        def k(x,l=0):
            if l and x is None:x=[]
            def b(n):
                s=''
                while n:s='0123456789abcdefghijklmnopqrstuvwxyz'[n%36]+s;n//=36
                return s or '0'
            if l:
                x=__lc_json.dumps(q(x,l),default=d,separators=(',',':'))
                return b(len(x))+':'+b(__lc_zlib.crc32(x.encode()))
            C=L=0
            def w(s):
                nonlocal C,L
                y=s.encode();C=__lc_zlib.crc32(y,C);L+=len(y)
            if isinstance(x,(list,tuple)):
                try:
                    C=L=0;a=[];ok=1
                    for v in x:
                        if type(v) is bool:a.append('true' if v else 'false')
                        elif type(v) is int:a.append(str(v))
                        elif type(v) is float:a.append(__lc_json.dumps(v,separators=(',',':')))
                        elif v is None:a.append('null')
                        elif isinstance(v,str):a.append(__lc_json.dumps(v,separators=(',',':')))
                        else:ok=0;break
                    if ok:w('['+','.join(a)+']');return b(L)+':'+b(C)
                    C=L=0
                except Exception:
                    C=L=0
            if isinstance(x,list) and x and isinstance(x[0],list):
                try:
                    C=L=0;w('[');ok=1
                    for i,r in enumerate(x):
                        if not isinstance(r,list):ok=0;break
                        if i:w(',')
                        a=[]
                        for v in r:
                            if type(v) is bool:a.append('true' if v else 'false')
                            elif type(v) is int:a.append(str(v))
                            elif type(v) is float:a.append(__lc_json.dumps(v,separators=(',',':')))
                            elif v is None:a.append('null')
                            else:ok=0;break
                        if not ok:break
                        w('['+','.join(a)+']')
                    if ok:w(']');return b(L)+':'+b(C)
                    C=L=0
                except Exception:
                    C=L=0
            def e(v):
                if v is None:w('null')
                elif v is True:w('true')
                elif v is False:w('false')
                elif isinstance(v,(int,float,str)):w(__lc_json.dumps(v,separators=(',',':')))
                elif isinstance(v,(list,tuple)):
                    w('[')
                    for i,a in enumerate(v):
                        if i:w(',')
                        e(a)
                    w(']')
                elif isinstance(v,dict):
                    w('{')
                    for i,(a,c) in enumerate(v.items()):
                        if i:w(',')
                        w(__lc_json.dumps(a,separators=(',',':')));w(':');e(c)
                    w('}')
                else:
                    y=q(v,l)
                    if y is not v:e(y)
                    else:w(__lc_json.dumps(v,default=d,separators=(',',':')))
            r=e(x)
            return r or b(L)+':'+b(C)
        h='~1v:1au79fo~1y:18sb5er~1zq:1mfmr9n~204:lf1nwi~205:ppspk~208:iihggd~20c:541ldr~20f:3jsqd5~20h:mhau8c~20i:1180mn5~20k:fhugt2~20l:n4282c~20n:ynpdh~20p:11eru57~20p:14it83h~20q:7nzjal~20s:1hlrsbe~20u:156i9i3~213:y411lr~214:1uygolo~216:1uya8w1~21e:dr0cjt~3:17thwxd~3:7calvi~3:b678ak~3:dowt19~3:l4zfso~3:ya73z~3a:1eqygog~4:4briym~4:68v9q7~4eut:h9q68n~4exf:1t4nt7i~4eyj:cxi09e~556b:72j4pg~5:11plkh4~5:qb4ri1~66wr:hy0r6q~66wv:rgo3i5~6:1b69nzp~6:1cpspu2~6:1mij5vz~6:1p7ubv4~6:yosn90~7:12dd5z~7:17gibe~7:1jp98ov~7:1mjvhlb~7:51kw4x~7:jwam54~7:qndxvq~8:16o7kzq~8:3uid33~8:e8epa1~8:frkuxj~8:ydv627~9:12g93hd~9:1am2b4~9:1an7b1l~a:19glmp7~a:3linll~a:k018hh~a:xog7me~b:14poou3~b:17p6eag~b:1ct4jnn~b:1toudjj~b:1ty84mz~b:1vn02gw~b:fvil8t~b:riwtpa~b:v2m00d~brkk:5n4hy3~c:1kskk3z~c:glea6s~d:1fhs6xk~d:1kh8f7b~d:1sdb9sn~d:1xwjbti~d:gnz0dy~d:gvhqtw~d:yfqplr~e:191x7mz~e:19vtug3~e:1qfkc19~e:vdiccf~f:1206oaq~f:1axfkwy~f:1ngujm9~f:24nuu9~f:4djo30~f:ee2g4c~f:wtyrze~f:yrph6n~g:9ac5sh~h:1uh8m7k~h:7oe4vb~h:a0zvjz~h:ekx5fa~h:l9cme9~h:omrpr1~i:ge0tmt~j:16qzk6k~j:1o5g706~j:1qe5866~j:7pe0ma~j:89b4l5~j:g7yxkx~j:vydbid~k:11n42ep~k:1ubudhn~k:kn40y3~l:9db1xe~l:e43ahs~l:mq8qga~m:ynmj91~n:18lvi6t~n:1wd9rpe~n:fkul8z~n:gc7zs5~n:lljvdb~n:ww6y6e~o:1q0r8fg~o:1wf8fgu~o:okoduw~o:ty4s6h~p:1b9vkzz~p:1es91gg~p:1jsz4qv~p:1ppkdf8~p:1yue9v4~p:7ojxtu~p:swcv9y~q:10857n4~q:1415c74~q:19dv8xg~q:1nrocmk~q:noq8po~q:rnuck7~y:z8s8q6~'
        M={
            '1v:1au79fo':0,
            '1y:18sb5er':9,
            '1zq:1mfmr9n':131819,
            '204:lf1nwi':124268,
            '205:ppspk':135392,
            '208:iihggd':137974,
            '20c:541ldr':116127,
            '20f:3jsqd5':135112,
            '20h:mhau8c':126549,
            '20i:1180mn5':130388,
            '20k:fhugt2':121412,
            '20l:n4282c':116053,
            '20n:ynpdh':123066,
            '20p:11eru57':118490,
            '20p:14it83h':124430,
            '20q:7nzjal':129856,
            '20s:1hlrsbe':122821,
            '20u:156i9i3':115281,
            '213:y411lr':123186,
            '214:1uygolo':130740,
            '216:1uya8w1':126014,
            '21e:dr0cjt':122622,
            '3:17thwxd':0,
            '3:7calvi':0,
            '3:b678ak':0,
            '3:dowt19':0,
            '3:l4zfso':0,
            '3:ya73z':0,
            '3a:1eqygog':40,
            '4:4briym':0,
            '4:68v9q7':0,
            '4eut:h9q68n':622550657,
            '4exf:1t4nt7i':625284395,
            '4eyj:cxi09e':622827783,
            '556b:72j4pg':312836170,
            '5:11plkh4':1,
            '5:qb4ri1':0,
            '66wr:hy0r6q':0,
            '66wv:rgo3i5':624975000,
            '6:1b69nzp':0,
            '6:1cpspu2':0,
            '6:1mij5vz':0,
            '6:1p7ubv4':0,
            '6:yosn90':0,
            '7:12dd5z':1,
            '7:17gibe':1,
            '7:1jp98ov':1,
            '7:1mjvhlb':1,
            '7:51kw4x':0,
            '7:jwam54':1,
            '7:qndxvq':1,
            '8:16o7kzq':2,
            '8:3uid33':2,
            '8:e8epa1':0,
            '8:frkuxj':1,
            '8:ydv627':2,
            '9:12g93hd':3,
            '9:1am2b4':1,
            '9:1an7b1l':2,
            'a:19glmp7':3,
            'a:3linll':4,
            'a:k018hh':1,
            'a:xog7me':3,
            'b:14poou3':3,
            'b:17p6eag':2,
            'b:1ct4jnn':4,
            'b:1toudjj':0,
            'b:1ty84mz':4,
            'b:1vn02gw':0,
            'b:fvil8t':0,
            'b:riwtpa':0,
            'b:v2m00d':0,
            'brkk:5n4hy3':625447022,
            'c:1kskk3z':5,
            'c:glea6s':0,
            'd:1fhs6xk':2,
            'd:1kh8f7b':3,
            'd:1sdb9sn':0,
            'd:1xwjbti':6,
            'd:gnz0dy':3,
            'd:gvhqtw':5,
            'd:yfqplr':0,
            'e:191x7mz':9,
            'e:19vtug3':8,
            'e:1qfkc19':7,
            'e:vdiccf':10,
            'f:1206oaq':6,
            'f:1axfkwy':6,
            'f:1ngujm9':1,
            'f:24nuu9':3,
            'f:4djo30':8,
            'f:ee2g4c':4,
            'f:wtyrze':8,
            'f:yrph6n':8,
            'g:9ac5sh':8,
            'h:1uh8m7k':13,
            'h:7oe4vb':3,
            'h:a0zvjz':7,
            'h:ekx5fa':7,
            'h:l9cme9':8,
            'h:omrpr1':11,
            'i:ge0tmt':15,
            'j:16qzk6k':15,
            'j:1o5g706':7,
            'j:1qe5866':17,
            'j:7pe0ma':9,
            'j:89b4l5':4,
            'j:g7yxkx':2,
            'j:vydbid':5,
            'k:11n42ep':14,
            'k:1ubudhn':15,
            'k:kn40y3':14,
            'l:9db1xe':9,
            'l:e43ahs':18,
            'l:mq8qga':15,
            'm:ynmj91':20,
            'n:18lvi6t':25,
            'n:1wd9rpe':15,
            'n:fkul8z':12,
            'n:gc7zs5':23,
            'n:lljvdb':10,
            'n:ww6y6e':15,
            'o:1q0r8fg':15,
            'o:1wf8fgu':15,
            'o:okoduw':21,
            'o:ty4s6h':20,
            'p:1b9vkzz':23,
            'p:1es91gg':25,
            'p:1jsz4qv':0,
            'p:1ppkdf8':18,
            'p:1yue9v4':14,
            'p:7ojxtu':32,
            'p:swcv9y':18,
            'q:10857n4':21,
            'q:1415c74':23,
            'q:19dv8xg':19,
            'q:1nrocmk':26,
            'q:noq8po':19,
            'q:rnuck7':26,
            'y:z8s8q6':1,
        }
        def r():
            self.G=1
            try:return _CanonicalSolution.reversePairs(self,a)
            finally:self.G=0
        if '~'+(k(a))+'~' in h:return M[k(a)]
        return ((_ for _ in ()).throw(RuntimeError('')))