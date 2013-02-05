"""
   _____                          __                 _________                  .___      
  /     \   ____   ____   _______/  |_  ___________  \_   ___ \_____ _______  __| _/______
 /  \ /  \ /  _ \ /    \ /  ___/\   __\/ __ \_  __ \ /    \  \/\__  \\_  __ \/ __ |/  ___/
/    Y    (  <_> )   |  \\___ \  |  | \  ___/|  | \/ \     \____/ __ \|  | \/ /_/ |\___ \ 
\____|__  /\____/|___|  /____  > |__|  \___  >__|     \______  (____  /__|  \____ /____  >
        \/            \/     \/            \/                \/     \/           \/    \/ 

types
gs  Grass
fe  Fire
wr  Water
lg  Lightning
pc  Psychic
fg  Fighting
cs  Colorless
dk  Dark
ml  Metal


Define Classes
"""
class Card:
    def __init__(self,name,number,movea,moveb):
        self.name = name
        self.number = number
        self.movea = movea
        self.moveb = moveb
 
    def getName(self):
        return self.name
 
    def getNumber(self):
        return self.number
 
    def getMoveA(self):
        return self.movea
 
    def getMoveB(self):
        return self.moveb

#THIS IS MURICA, IMPORT STUFF
import pprint

import yaml
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
        
#Get language file
langFile = open('lang_sentences.yml')
langObj = load(langFile, Loader=Loader)
pprint.pprint(langObj)


cardSetFile = open('base.set')
cardSet = yaml.load(cardSetFile)
for card in cardSet:
    pprint.pprint(card)
#pprint.pprint(cardSet)

aCard = Card("JigglyPuffy",39,"Pound","none")
print aCard.getName(),langObj['used'],aCard.getMoveA()+"!",langObj['supereffective']


































