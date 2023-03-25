projet python: oil race


But : réaliser un jeu d'arcade à la vue de dessus (top down) où le joueur pilote une voiture. 
Objectif joueur : maintenir sa voiture le plus longtemps possible sur la route avant le game over.

Eléments:
voiture:  - 5 voiture différentes : voiture, voiture de course, camion, hot-road, voiture tunée
		- faire un écran de choix
	  - doit avoir une hitbox
	  - ralentit lorsqu'il est : en panne d'essence (jusqu'à l'arret) ou sur l'herbe.
	  - a différentes caractéristiques telles que : la puissance, le réservoir et la nitro
	  - doit recharger sa barre de réservoir à l'aide d'essence

route :	  - défilement verticale vers le bas
	  - composée d'une route goudronnée et d'herbe
	  - taille nécessaire pour faire apparaitre le véhicule, les bonus et les ennemis

enemis :  - deux types d'ennemis: les hooligans et la police

		- les holigans : - hitbox
				 - se déplace vers le bas
				 - pas plus de deux voitures
				 - un coup = game over
				 - disparait une fois le bas touché

		- la police : - hitbox
			      - arrive que lorsque le joueur utilise trop la nitro (3 fois) et roule sur l'herbe
			      - se déplace vers le haut
			      - un coup = game over
			      - disparait en utilisant la nitro (1 coup) avant 30s

power up:  - deux types de power up : le carburant et la nitro.

		- le carburant : - permet de recharger la barre de carburant
				 - hitbox
				 - défile vers le bas
				 - fréquence d'apparition : de plus en plus rare au fil du jeu

		- la nitro : - permet de recharger la barre de nitro
			     - hitbox
			     - défile vers le bas
			     - fréquence d'apparition : 1 après une certaine distance

caractéristique : - trois types la puissance, le réservoir et la nitro

			- la puissance : - constante (pour la voiture)
					 - défilement de la route
					 - diférent pour chaque voiture

			- le réservoir : - variable
					 - baisse de 20 % après une certaine distance parcouru
					 - recharge de 20 % si on touche le carburant
					 - différent pour chaque véhicule

			- la nitro : - variable
				     - accélère le défilement sur un certain temps
				     - baisse d'une barre si la nitro est utilisé
				     - recharge d'une barre si on touche à la nitro
				     - différent pour chaque véhicule

		  - caractéristique différentes voiture :
			- voiture : vitesse 100, réservoir 100, nitro 5
			- voiture de course : vitesse 200, réservoir 100, nitro 5
			- camion: vitesse 100, réservoir 200, nitro 5
			- hot-road: vitesse 200, réservoir 200, nitro 10
			- voiture tuné : vitesse 200, réservoir 100, nitro 10

game over : - game over si:
		- percute un hooligan
		- se fait rattraper par la police (utilise la nitro après le temps imparti)
		- tombe en rade d'essence.
		