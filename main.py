"""Imports et définition des variables globales"""


#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    char=[s[0]]
    o=[1]
    n=len(s)
    k=1
    while k<n:
        if s[k]==s[k-1]:
            o[-1]+=1
        else:
            char+=[s[k]]
            o+=[1]
        k=k+1
    return list(zip(char,o))


def artcode_r(s,lst=None):
    """retourne la liste de tuples selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    if lst is None:
        lst=[]
    if len(s)==0:
        return lst
    char=s[0]
    count=1
    for i in range(1,len(s)):
        if s[i]==char:
            count+=1
        else:
            break
    lst.append((char,count))
    return artcode_r(s[count:],lst)
    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
#### Fonction principale


def main():
    """fct principale test le programme"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
