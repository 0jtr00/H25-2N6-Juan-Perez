# Q1                                                                                                            #
# créez une nouvelle liste de 4 à 5 sports et imprimez la liste                                                         #
print(f"Q1{'_'*60}")
sports = ['basket', 'danse', 'natation', 'volleyball']


# Q2                                                                                                             #
# affichez le premier sport de votre liste (en utilisant son index)                                                                     #
print(f"Q2{'_'*60}")
print(sports[1])



# Q3                                                                                                             #
# ajoutez un nouveau sport à la fin de la liste avec la méthode append                                                               #
# et affichez le dernier sport que vous avez dans la liste                                                       #
print(f"Q3{'_'*60}")
sports.append('jujutsu')
print(sports[4])




# Q4 ajoutez un nouveau sport après le 1er sport de votre liste avec la méthode insert 
#    puis imprimez la liste                                                 #
                                                                 # 
print(f"Q4{'_'*60}")
sports.insert(1, 'foot')
print((sports))



# Q5
#  La variable "autres_sports" contient 3 valeurs                                                                    # 
#    ajoutez ces 3 valeurs à votre liste de sports avec la méthode extend                                            #
#    imprimez la liste telle qu'elle est rendue
print(f"Q5{'_'*60}")
autres_sports = ["Quiddich", "rodeo", "parcour"]
sports.extend(autres_sports)
print(sports)


#  Q6                                                                                                               #
#  Imprimez le nom d'un sport que vous enlèverez ensuite de la liste                                                #
#  Enlevez un sport de la liste avec remove                                                                         #
#  Imprimez la liste et voyez que le sport que vous avez enlevé avec remove est bel et bien enlevé  
print(f"Q6{'_'*60}")
print("J'ai enlevé Quiddich ")
sports.remove('Quiddich')
print(sports)
#  Q7
#  Enlever le dernier sport de la liste avec pop. Le sport enlevé est retourné par pop Affichez-le                  #
#  Imprimez la liste en spécifiant le sport enlevé et utilisant f-string                                            #
print(f"Q7{'_'*60}")
sports.pop()
print(f"{sports}.\n")




# Q8                                                                                                             #
# Utilisez une boucle for pour passer à travers chaque sport dans la liste avec une boucle for                   #
# et affichez le sport sur différentes lignes                                                                    #
print(f"Q8{'_'*60}")
for sport in sports :
    print(sport)



 
  
# Q9                                                                                                             #
# Ordonner la liste en ordre croissant avec la méthode sort et imprimez-la                                       #
print(f"Q9{'_'*60}")
sports.sort()
print(sports)











# Q10                                                                                                                 #
# Imprimez une sous-liste des deux premiers sports, en utilisant le slicing                                          #
print(f"Q10{u'_'*60}")
print(sports[:2])