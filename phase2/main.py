import random

from hero_class import Hero

cjsh = Hero()

cjsh.alias = '苍狼末裔'
cjsh.name = '成吉思汗'
cjsh.position = '射手ARCHER'
cjsh.ab_viability = random.randint(1,100)
cjsh.ab_damage = random.randint(1,100)
cjsh.ab_effect = random.randint(1,100)
cjsh.ab_difficulty = random.randint(1,100)

cjsh.show_story()
cjsh.show_presentation()
cjsh.show_history()
