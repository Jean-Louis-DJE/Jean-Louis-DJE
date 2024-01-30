#CODE BY JEAN-LOUIS DJE

def computeMultipleSum(n):
    if n>=0 & n<1000 :
        k=1
        sum=0
        while k <= n :
            if k%3 == 0:
                sum += k
            if k%5 == 0:
                sum += k
            if k%7 == 0:
                sum += k
            k += 1
        return sum
    else:
        return -1

def computeJoinPoint(s1, s2):
    if s1>0 & s2<20000000:
        s1_li = [-1] #listes de comparaison
        s2_li = [-2] #listes de comparaison
        sums1 = 0 #nombre suivant de la sequence de s1
        sums2 = 0 #nombre suivant de la sequence de s2
        retour = 0 #variable de retour

        test = false

        while not test :

            s1_str = string(s1)
            s2_str = string(s2)

            #Somme des chiffres
            for i in s1_str:
                sums1 += int(i)
            for i in s2_str:
                sums2 += int(i)

            #ajout aux listes de comparaison
            sums1 += s1
            s1_li.append(sums1)
            sums2 += s2
            s2_li.append(sums2)

            #mise à jour
            s1 = sums1
            s2 = sums2

            #on vérifie si le joint point à été trouvé
            for element in s1_li:
                if element in s2_li:
                    test = true
                    retour = element
            
    else:
        return -1

   











