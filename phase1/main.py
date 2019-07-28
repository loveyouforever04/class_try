from my_01_class import Myclass

me = Myclass()

if me.sex == '男':
    print('my name is %s, I am a boy.'%me.name)
elif me.sex == '女':
    print('my name is %s, I am a girl.'%me.name)
else:
    print('my name is %s, I am a ...'%me.name)

me.work()
me.study()
