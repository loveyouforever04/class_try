import random
class Hero():

    def __init__(self,s,n,p):
        '''初始化函数'''

        if len(s) >0 and len(n)>0 and len(p)>0:
            self.skin =  s
            self.name = n
            self.name = p

            self.ab_viability = random.randint(1,100)
            self.ab_damage = random.randint(1,100)
            self.ab_effect = random.randint(1,100)
            self.ab_difficulty = random.randint(1,100)
        else:
            self.skin = '英雄的皮肤'
            self.name = '英雄的姓名'
            self.name = '英雄的定位'

            self.ab_viability = 0
            self.ab_damage = 0
            self.ab_effect = 0
            self.ab_difficulty = 0
        return
    '''
    skin = '英雄的原始皮肤'
    name = '英雄的姓名'
    position = '英雄的定位'
    ab_viability = 0
    ab_damage = 0
    ab_effect = 0
    ab_difficulty= 0
    '''
    def show_presentation(self):
        print('\n英雄的介绍,xxxxxxxx')
        print('\n生存的能力=[%d],攻击伤害=[%d],技能效果=[%d],上手难度=[%d]'%(self.
        ab_viability,self.ab_damage,self.ab_effect,self.ab_difficulty))
        return

    def show_story(self):
        print('\n英雄的故事，xxxxxxxx')
        return

    def show_history(self):
        print('\n史实中的英雄，xxxxxxxx')
        return
