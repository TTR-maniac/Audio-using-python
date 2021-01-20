
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 
# What You want to make the book say on engine.say
engine.say('Chapter 1 page one I am a hacker. And my name is Adam You can just call me Anon It means anonymous. Cuz I hack so blah blah blah let sget that over with I use bash and other things to hack with but I also code in python. I am currently lerning it. So What I.D.E should I use it is your choice there are many to choose from. If you code in python I realy reccomend pycharm but anything else its your choice. You can use eclipse visual studio code. ANYTHING. So wht game engine should I use it matters. For  people who like prorfessional look or basic unity. simple or not simple 3d and 2d projects on unity. And same as go dot but I dont realy use it. I am not jusing you if there i any other engine you want to incluede in this python book. Oh wait Also use cryengine and unreal game engine. Thats all so if you wanna edit this book go for it ')
engine.runAndWait()

