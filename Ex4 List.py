# Q1                                                                                                                   #
# Créez une liste de 3 modèles de cartes graphiques. Voici une liste de cartes graphiques. Vous pouvez construire votre liste en choisissant parmi les suivantes:
#          GeForce RTX 3090Ti, GeForce RTX 3080Ti, GeForce RTX 3070Ti, Radeon RX 6950 XT, Radeon RX 6900 XT, Radeon RX 6800 XT             
# Vous pouvez aussi mettre un autre modèle de carte graphique si vous voulez.#
# imprimez la liste                                                                                                    #
print(f"Q1{u'_'*60}")
carte_graphique = ['GeForce RTX 3090Ti', 'GeForce RTX 3080Ti', 'GeForce RTX 3070Ti']
print(carte_graphique)



#Q2                                                                                                                   #
#  Obtenez la carte graphique à l'index 1 de la liste de vos cartes graphiques                                        #
#  Enlevez-la de la liste                                                                                             #
#  Imprimez la liste en spécifiant l'item enlevé                                                                      #
print(f"Q2{u'_'*60}")
carte_graphique1 = carte_graphique[0]
carte_graphique.remove(carte_graphique1)
print(carte_graphique)





# Q3                                                                                                                   #
# Ajoutez un nouvel item à la fin de la liste                                                                          #
# et affichez la dernière carte graphique que vous avez maintenant dans la liste                                       #
print(f"Q3{u'_'*60}")
carte_graphique.append('Radeon RX 6950 XT')
print(carte_graphique[2])




# Q4                                                                                                                 #
# Inversez les items de votre liste                                                                                  #
print(f"Q4{u'_'*60}")
carte_graphique.reverse()
print(carte_graphique)


# Q5                                                                                                                 #
# Créez une petite liste de deux nouvelles cartes graphiques                                                         #
# Imprimez cette nouvelle petite liste                                                                               #
# Ajoutez cette nouvelle petite liste à la fin de votre première liste                                               #
# Imprimez votre liste initale telle qu'elle est rendue                                                              #
print(f"Q5{u'_'*60}")
carte_graphique2 = ['carte1', 'carte2']
carte_graphique.extend(carte_graphique2)
print(f"JJ,{carte_graphique}")




# Q6                                                                                                                  #
# Ordonnez la liste en ordre croissant de façon à créer une nouvelle liste                                            #
# et imprimez cette nouvelle liste                                                                                    #
print(f"Q6{u'_'*60}")
carte_graphique3 = carte_graphique.sort()
print(carte_graphique3)





