// not my code, just wanted to try something out
// source: https://www.arndt-bruenner.de/mathe/scripts/periodenlaenge.htm


var pz=new Array(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083, 3089, 3109, 3119, 3121, 3137, 3163);



function periodenlaenge(N)
{
	if(N==1)return 0;
	if(N<2)return "?";
	var basis=10;
	if(N!=Math.floor(N))return;
	if(isNaN(N))return;
	var n=N,PFStr="",i;
	var PF=(PFStr=pfz(basis)).split("·");
	for(i=0;i<PF.length;i++){while(n%PF[i]==0)n/=PF[i];}
	if(n==1)return 0;
	var p=phi(n);
	var tm=getTeiler(p),i;
	for(i=0;i<tm.length;i++)
	{
		var pm=modpow(basis,tm[i],n);
		if(pm==1)break;
	}
	return tm[i];
}


function pfz(n)
{
	if(n>100000000){alert(n+" ist zu groß");return;}
	var i,t="";
	for(i=0;i<pz.length;i++){while(n%pz[i]==0){n/=pz[i];t+=pz[i]+"·";}if(n==1)break;}
	if(n>3162)t+=n+" ";
	return t.substr(0,t.length-1);
}
var phi_faktoren=new Array();
function phi(n)
{
	if(n==1)return 1;
	var fz=pfz(n).split("·"),p=fz[0]-1,i;
	phi_faktoren=new Array(fz.length);phi_faktoren[0]=p;
	for(i=1;i<fz.length;i++){if(fz[i]==fz[i-1])p*=(phi_faktoren[i]=fz[i]);else p*=(phi_faktoren[i]=fz[i]-1);}
	return p;
}

function modpow(b,e,m)
{
	if(e==0)return 1;
	var L=Math.floor(Math.log(e)/Math.log(2)+1);
	var p=1;
	b%=m;
	for(var i=L-1;i>=0;i--)
	{
		var a=((e&bin[i])>0);
		if(a)p=(p*b)%m;
		if(i>0)p=(p*p)%m;
	}
	return p;
}
function getTeiler(N)
{
	var fz=pfz(N).split("·"),i,j=0,k=0;
	if(fz.length==0)return null;
	var prfn=new Array(),nprf,prf=new Array();
	if(N<=1){prf[0]=1;return prf;}
	prf[k]=fz[0];prfn[k]=1;
	for(i=1;i<fz.length;i++)
	{
		if(fz[i-1]==fz[i])prfn[k]++; else {k++;prfn[k]=1;prf[k]=fz[i];}
	}
	var nprf=prf.length; n=prfn[0]+1;for(i=1;i<nprf;i++)n*=(prfn[i]+1);
	var T=new Array(n);
	for(i=0;i<n;i++)T[i]=1;
	k=prfn[0]+1;
	var p=prf[0];
	var pp=1;
	for(i=0;i<prfn[0];i++){pp*=p;T[i+1]=pp;}
	for(i=1;i<nprf;i++) //Schleife über alle Primfaktoren
	{
		p=prf[i];pp=p;
		for(j=0;j<prfn[i];j++) //Schleife über alle Potenzen des Primfaktors
		{
			var d=j*k+k,a;
			for(a=0;a<k;a++){T[a+d]=T[a]*pp;}
			pp*=p;
		}
		k*=(prfn[i]+1);
	} 
	quicksort(T);
	return T;
}


function quicksort(A)
{
    L=new Array(32),R=new Array(32);
    var s, i, j, LL, rr, v, w, ii;
    s=0; L[0]=0; R[0]=A.length-1;
    do
    {
        LL = L[s]; rr = R[s];
        s--;
        do
        {
            i = LL; j = rr;
            v = A[Math.floor((LL + rr) / 2)];
            do
		{
                while(A[i]<v) i++;
                while(A[j]>v) j--;
                if (i <= j)
                {
                    w = A[i]; A[i] = A[j]; A[j] = w;
                    i++; j--;
                }
            } while (i <= j);
            if (j - LL >= rr - 1)
            {
                if (LL < j)
                {
                    s++;
                    L[s] = LL; R[s] = j;
                }
                LL = i;
            }
            else
            {
                if (i < rr)
                {
                    s++;
                    L[s] = i; R[s] = rr;
                }
                rr = j;
            }
        } while (LL < rr);
    } while (s >= 0);
}
