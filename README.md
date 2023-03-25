# Oil race

## Objectif du projet 

Réaliser un jeu d'arcade en vue de dessus (top down) où le joueur pilote une voiture. 
L'objectif du joueur est de parcourir la plus grande distance possible avant le game over.

## Game Over :

Le joueur pert dès lors qu'il
- percute un 'hooligan'
- se fait rattraper par la police
- tombe en rade d'essence

## Principes de jeu:

### Les voitures   
- 5 voitures différentes : voiture, voiture de course, camion, hot-road, voiture tunée
- ralentit si
  * en panne d'essence (jusqu'à l'arret) 
  * roule sur l'herbe
- chaque vehicule a différentes caractéristiques 
  * la puissance (la vitesse à laquelle elle accélère)
	- constante (pour la voiture)
	- défilement de la route
	- diférent pour chaque voiture
  * sa vitesse maximale
  * la taille du réservoir d'essence
	- variable
	- baisse de 20 % après une certaine distance parcouru
	- recharge de 20 % si on touche le carburant
	- différent pour chaque véhicule
  * le nombre de coups de nitro possibles
	- variable
	- accélère le défilement sur un certain temps
	- baisse d'une barre si la nitro est utilisé
	- recharge d'une barre si on touche à la nitro
	- différent pour chaque véhicule

### Caractéristiques des différents véhicules
- voiture : vitesse 100, réservoir 100, nitro 5
- voiture de course : vitesse 200, réservoir 100, nitro 5
- camion: vitesse 100, réservoir 200, nitro 5
- hot-road: vitesse 200, réservoir 200, nitro 10
- voiture tuné : vitesse 200, réservoir 100, nitro 10

### La route 
- défilement verticale vers le bas
- composée d'une route goudronnée et d'herbe

### Les ennemis :  - deux types d'ennemis: les hooligans et la police
- les holigans : 
  * se déplace vers le bas (i.e. en sens inverse)
  * pas plus de deux ennemis à la fois
  * un coup = game over
  
- la police : 
  * n'apparait que lorsque le joueur utilise trop souvent la nitro (3 fois) ou roule sur l'herbe
  * se déplace vers le haut
  * un coup = game over
  * disparait en utilisant la nitro (1 coup) avant 30s

### Les aides / power up:

Deux types de power up : le carburant et la nitro.

- le carburant : 
  * permet de recharger la barre de carburant
  * défile vers le bas
  * fréquence d'apparition : de plus en plus rare au fil du jeu

- la nitro : 
  * permet de recharger la barre de nitro
  * défile vers le bas
  * fréquence d'apparition : 1 après une certaine distance
		