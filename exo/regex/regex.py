
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

#Silicon_Valley-s01e01-Minimum_Viable_Product.avi
#Silicon_Valley-s01e02-The_Cap_Table.avi
#Silicon_Valley-s01e03-Articles_Of_Incorporation.avi
#Mr_Robot-s02e07-H4ndshake.mp4
#Mr_Robot-s02e09-Init5.mp4
#Breaking_Bad-s04e05-Shotgun.avi
#Breaking_Bad-s04e08-Hermanos.avi
#Supergirl-s01e01-Pilot.mkv

float_regex	=	re.compile('^(?P<titre_serie>[a-zA-Z_0-9]*)-(?P<saison>^s[0-9]{2})(?P<episode>^e[0-9]{2})-(?P<titre_episode>[a-zA-Z_0-9]*)\.(?P<extension>[a-zA-Z]{3})$')
ma_chaine	=	'Silicon_Valley-s01e01-Minimum_Viable_Product.avi'
resultat	=	float_regex.search(ma_chaine)


titre_serie = resultat.group('titre_serie')
saison = resultat.group('saison')
episode = resultat.group('episode')
titre_episode = resultat.group('titre_episode')
extension = resultat.group('extension')

print ("Le titre de la série est: {} \n Le numéro de la saison est: {} \n Le numéro de l'épisode est {} \n Le titre de l'épisode est {} \n Le format est: {}".format(titre_serie, saison, episode, titre_episode, extension)  )

