#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import hashlib
import os
import sys

banniere = """
\033[0;95m ___                       _    ___             _   \033[0;92m_____         _ 
\033[0;95m|   \ ___ __ _ _ _  _ _ __| |_ / __|_ _ __ _ __| |_\033[0;92m|_   _|__  ___| |
\033[0;95m| |) / -_) _| '_| || | '_ \  _| (__| '_/ _` / _| / / \033[0;92m| |/ _ \/ _ \ |
\033[0;95m|___/\___\__|_|  \_, | .__/\__|\___|_| \__,_\__|_\_\ \033[0;92m|_|\___/\___/_|
\033[0;95m                  |__/|_|        Dev par \033[0;92mFlavien\033[0;95m, \033[0;92mMatthéo \033[0;95met \033[0;92mJordan
\033[0;95m                                 Tapez la commande \033[0;92m.aide \033[0;95mpour commencer

"""
aide = """
\033[0;95m         ->       Voici les différents \033[0;92m commandes\033[0;95m        <-
\033[0;95m\033[0;92m[+]\033[0;95m══════════════════════════════════════════════════════════════\033[0;92m[+]\033[0;95m
\033[0;95m ║    \033[0;95m.\033[0;92maide          \033[0;95m=      \033[0;95mAffiche les \033[0;92mcommandes \033[0;95mde bases\033[0;95m        ║
\033[0;95m ║    \033[0;95m.\033[0;92mmethodes      \033[0;95m=      \033[0;95mAffiche les \033[0;92mméthodes \033[0;95mdes modules\033[0;95m      ║
\033[0;95m ║    \033[0;95m.\033[0;92minfo          \033[0;95m=      \033[0;95mAffiche les \033[0;92minfos \033[0;95msur le programme\033[0;95m    ║
\033[0;95m ║    \033[0;95m.\033[0;92mclear         \033[0;95m=      \033[0;95mEfface la \033[0;92mconsole \033[0;95m                    ║      
\033[0;95m ║    \033[0;95m.\033[0;92mexit          \033[0;95m=      \033[0;95mPermet de \033[0;92mquitter \033[0;95mle programme\033[0;95m        ║                        
\033[0;95m\033[0;92m[+]\033[0;95m══════════════════════════════════════════════════════════════\033[0;92m[+]\033[0;95m
"""
info = """
\033[0;95mProgramme codé par \033[0;92mFlavien\033[0;95m, \033[0;92mMatthéo \033[0;95met \033[0;92mJordan\033[0;95m.

\033[0;95mCe programme est un \033[0;92mprojet de NSI\033[0;95m, qui à pour finalité de permettre :

    - De \033[0;92mchiffrer\033[0;95m des messages avec sa propre fonction affine, 
        puis permet de trouver le fonction de \033[0;92mdéchiffrement\033[0;95m pour décoder les messages.
    - De \033[0;92mhasher\033[0;95m des chaine de caractère selon les fonctions principales 
        comme MD5, SHA ... Mais aussi par attaque bruteforce, de pouvoir \033[0;92mdéhasher\033[0;95m.
"""

def MenuBase():
    gauche = "\033[0;95m>>> \033[0;92m"
    choixMethodes = """ 
    \033[0;95m          ->       Voici les différents \033[0;92m modules\033[0;95m        <-                 
    \033[0;95m\033[0;92m[+]\033[0;95m══════════════════════════════════════════════════════════════\033[0;92m[+]\033[0;95m
    \033[0;95m ║    \033[0;95m.\033[0;92mchiffrement   \033[0;95m=      \033[0;95mModule \033[0;92mChiffrement \033[0;95m/ \033[0;92mDéchiffrement\033[0;95m    ║
    \033[0;95m ║    \033[0;95m.\033[0;92mhashage       \033[0;95m=      \033[0;95mModule \033[0;92mHashage \033[0;95m/ \033[0;92mDéhashage\033[0;95m            ║                            
    \033[0;95m\033[0;92m[+]\033[0;95m══════════════════════════════════════════════════════════════\033[0;92m[+]\033[0;95m
    """
    while True:
        entrerGauche = input(gauche).lower()
        entrer = entrerGauche.split(" ")[0]
        if entrer == ".aide":
            print(aide)
        elif entrer == ".methodes":
            print(choixMethodes)
        elif entrer == ".info":
            print(info)
        elif entrer == ".clear":
            os.system("cls")
            main()
        elif entrer == ".exit":
            print("\033[0;92mMerci d'avoir utilisé notre programme !\033[0;92m")
            exit()
        elif entrer == ".chiffrement":
            return "chiffrement"
        elif entrer == ".hashage":
            return "hashage"

def hashageMenu():
    os.system("cls")
    print(banniere)
    typeHash = ["shake_128","blake2b","sha384","md5","sha3_224","sha3_384","sha512","sha224","blake2s","sha3_256","shake_256","sha256","sha1","sha3_512"]
    print(""" 
    \033[0;95m ->       Voici les différents \033[0;92mfonctionnalités\033[0;95m du modules\033[0;95m        <-                 
    \033[0;95m\033[0;92m[+]\033[0;95m══════════════════════════════════════════════════════════════\033[0;92m[+]\033[0;95m
    \033[0;95m ║    \033[0;95m.\033[0;92mhasher   \033[0;95m=      \033[0;95mPermet de \033[0;92mHasher \033[0;95mune chaine de caractère  ║
    \033[0;95m ║    \033[0;95m.\033[0;92mdehasher       \033[0;95m=      \033[0;95mPermet de \033[0;92mdéhasher \033[0;95mun hash           ║
    \033[0;95m ║    \033[0;95m.\033[0;92mquitter       \033[0;95m=      \033[0;95mPermet de \033[0;92mquitter \033[0;95mle module           ║                            
    \033[0;95m\033[0;92m[+]\033[0;95m══════════════════════════════════════════════════════════════\033[0;92m[+]\033[0;95m
    """)
    entrerGauche = input("\033[0;95m>>> \033[0;92m").lower()
    entrer = entrerGauche.split(" ")[0]
    if entrer == ".hasher":
        print("\n\033[0;95mVoici les différentes \033[0;92mfonctions de hash \033[0;95mdu tool, \nchoisissez votre fonction (Tapez le nombre correspondant): \n")
        for x in range(len(typeHash)):
            print("\033[0;95m-\033[0;92m", x, "\033[0;95m: Fonction\033[0;92m", typeHash[x].upper())
        choixHash = int(input("\n\033[0;95m>>> \033[0;92m"))
        for x in range(len(typeHash)):
            if choixHash == x:
                chaineCaractere = str(input("\n\033[0;95mEntrez votre \033[0;92mchaine de caractère\033[0;95m : \033[0;92m"))
                print("\n\033[0;0m[+] \033[0;95mHashage de votre chaine de caractère en cour ...")
                print("\033[0;0m[+] \033[0;32mHashage réussit\033[0;95m, voici le hash de\033[0;92m", chaineCaractere,"\033[0;95men\033[0;92m", typeHash[x],"\033[0;95m:\033[0;92m", hashage(chaineCaractere,x))
                continuer = input("\n\033[0;95mAppuyer sur une touche pour continuer ...")
                hashageMenu()
    elif entrer == ".dehasher":
        print("\n\033[0;95mPour cette fonctionnalité, le programme va utiliser l'attaque par bruteforce. \nUne wordlist de base est déjà présente, mais je conseil de la remplacer par celle de votre choix. \nVous devez donc placer la votre à la racine de ce dossier sous le nom de \033[0;92m'wordlist.txt'\033[0;95m.")
        print("\033[0;95mVoici les différentes \033[0;92mfonctions de hash \033[0;95mdu tool, \nchoisissez votre fonction (Tapez le nombre correspondant): \n")
        for x in range(len(typeHash)):
            print("\033[0;95m-\033[0;92m", x, "\033[0;95m: Fonction\033[0;92m", typeHash[x].upper())
        choixHash = int(input("\n\033[0;95m>>> \033[0;92m"))
        for x in range(len(typeHash)):
            if choixHash == x:
                hashUtilisateur = str(input("\n\033[0;95mEntrez votre \033[0;92mhash\033[0;95m : \033[0;92m"))
                print("\n\033[0;0m[+] \033[0;95mDehashage par bruteforce de votre hash en cour (cette action peut prendre du temps)...")
                wordlistEmplacement = open("wordlist.txt",'r')
                for i in wordlistEmplacement.readlines():
                    mot = i.strip("\n")
                    test = hashage(mot,x)
                    if test == hashUtilisateur:
                        print("\033[0;0m[+] \033[0;32mAttaque réussite\033[0;95m, voici votre hash déhashé :\033[0;92m", i)
                        continuer = input("\n\033[0;95mAppuyer sur une touche pour continuer ...")
                        hashageMenu()
                print("\033[0;0m[+] \033[1;31mAttaque ratée\033[0;95m, la wordlist ne comporte pas le mot du hash.")
                continuer = input("\n\033[0;95mAppuyer sur une touche pour continuer ...")
                hashageMenu()
    elif entrer == ".quitter":
        main()
    else:
        hashageMenu()

def hashage(chaineDeCaractere, hashNumero):
    if hashNumero == 0:
        x = hashlib.shake_128(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 1:
        x = hashlib.blake2b(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 2:
        x = hashlib.sha384(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 3:
        x = hashlib.md5(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 4:
        x = hashlib.sha3_224(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 5:
        x = hashlib.sha3_384(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 6:
        x = hashlib.sha512(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 7:
        x = hashlib.sha224(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 8:
        x = hashlib.blake2s(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 9:
        x = hashlib.sha3_256(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 10:
        x = hashlib.shake_256(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 11:
        x = hashlib.sha256(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 12:
        x = hashlib.sha1(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()
    if hashNumero == 13:
        x = hashlib.sha3_512(str(chaineDeCaractere).encode('utf-8'))
        return x.hexdigest()

def main():
    os.system("cls")
    nomFenetre = "\x1b]2;DecryptCrackTool\x07"
    print(banniere)
    sys.stdout.write(nomFenetre)
    choix = MenuBase()
    if choix == "chiffrement":
        chiffrementMenu()
    if choix == "hashage":
        hashageMenu()


main()
x = hashlib.sha256(b"admin")
print('Output 2 :', x.hexdigest())