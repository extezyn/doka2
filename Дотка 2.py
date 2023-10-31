
import random

TeamMood = 0

def static():
    print("Твои характеристики:""\nпонимание игры", stats[0],"\nлайнинг",stats[1],"\nмикроконтроль",stats[2],"\nигровой интелект",stats[3],"\nфарм",stats[4],"\nглупые смерти",stats[5])

def opponentTeam():
    i=0
    for i in range(len(teams)):
        print("Команды против вас", team[i])
        i+=1
    
def otdyh():
    i=0
    for i in range(len(stats)):
         print(stats[i]-1)

def training():
    i=0
    for i in range(len(stats)):
         print(stats[i]+1)


teams = ["Virtus Pro", "Bestcoast", "LGD", "QUEST", "NaVi" ]
players = [ "1.Dyrachyo","2.Мой игрок"]

print("Welcome to the DOTA 2 life ")
print("Ты проживешь целый сезон за игрока из профессиональной команды")


for i in range(len(players)):
    print(players[i],end=" ")

player = 2

if player ==1:
    try:
        Name = "Антон"
        Surname = "Шкредов"
        Nick = "dyrachyo"
        TeamMood = 50
        team = teams[random.randint(0, 4)]
        print("Вы выбрали {} {} {}".format(Name,Nick, Surname))
        print("Вы играете за команду Gaiming Gladiators")
        stats = [7, 7, 8, 9, 8, 5]  #понимание игры, лайнинг, микроконтроль, игровой интелект,фарм, глупые смерти
        print("понимание игры =", 
                    stats[0],", лайнинг =",
                    stats[1],", микроконтроль =",
                    stats[2],", игровой интелект =",
                    stats[3],", фарм =",stats[4],", глупые смерти =",stats[5])
        print("\nСейчас идет 1ый DPC сезон. Чтобы пройти квалы на мажор нужно занять 1, 2 или 3 место иначе на мажор вы не едете\n")
    except : 
        print("Invalid input")

    try:
        ponyal = input("понял?(да) \n")
        if ponyal == "да":
            win = 0
            i=1
            for i in range(3):
                print(i+1,"ая игра против ", team)
                WinChance = random.randint(0,100)
                if WinChance > 10 and WinChance <75:
                    print("В потнейшей игре, находясь на краю поражения вам удалось переломить ход игры и победить ", team)
                    TeamMood = TeamMood + 10
                    win+=1
                
                elif WinChance > 75:
                    print("Супер легкая победа для вас. Грац")
                    TeamMood = TeamMood + 5
                    win+=1

                else:  
                    print("У вас почти получилось выиграть. Не расстраивайтесь ведь впереди много побед")
                    TeamMood = TeamMood - 10

                y=4
                team = teams[random.randint(0, y)]
                teams.remove(team)
                i+=1
                y-=1
        else:
            while ponyal != "да":
                 ponyal = input("понял?(да) \n")
    except :
         print("Invalid input")

    try:  
        ponyal = input("Круто?(очень) \n")

        if ponyal == "круто":
            
            if win > 0 :
                print("Красавцы вы отобрались на мажор")
                print("Ты также вырос как игрок и можешь вкачать свои статы")
                print("Сейчас они выглядят вот так:")
                print("понимание игры =", 
                    stats[0],", лайнинг =",
                    stats[1],", микроконтроль =",
                    stats[2],", игровой интелект =",
                    stats[3],", фарм =",stats[4],", глупые смерти =",stats[5])
                choiceStats = input("Введите какую стату хоите вкачать ")
                if choiceStats == "понимание игры":
                    stats[0]+=1
                elif choiceStats == "лайнинг":
                    stats[1]+=1
                elif choiceStats == "микроконтроль" :
                    stats[2]+=1
                elif choiceStats == "игровой интелект":
                    stats[3]+=1
                elif choiceStats == "фарм":
                    stats[4]+=1
                elif choiceStats == "глупые смерти" and stats[5] != 0:
                    stats[5]-=1
                
                print("Так. Ты апнул характеристики:")
                print("понимание игры =", 
                    stats[0],", лайнинг =",
                    stats[1],", микроконтроль =",
                    stats[2],", игровой интелект =",
                    stats[3],", фарм =",stats[4],", глупые смерти =",stats[5])
            print("Ты стал сильнее как и твоя команда")
            ponyal = input("Четко? ")

        else:
            while ponyal != "очень":
                ponyal = input("Круто?(очень) \n")
    except :
        print("Invalid input")    
    
    try:
        print("\nТеперь нужно немного отдохнуть!")
        otdyh()
        print("После отдыха вы чуток потеряли форму\n"
            "чтобы вернуть форму надо потренить")
        trenyamb = input("Будешь тренироваться(да\нет)")
        if trenyamb == "да":
            training()
            print("Умничка\n")
            print("Апнулся.\nпонимание игры =", 
                stats[0],", лайнинг =",
                stats[1],", микроконтроль =",
                stats[2],", игровой интелект =",
                stats[3],", фарм =",stats[4],", глупые смерти =",stats[5])
        else:
           
            print("Ваш скил ухудшился",stats[0],", лайнинг =",
                stats[1],", микроконтроль =",
                stats[2],", игровой интелект =",
                stats[3],", фарм =",stats[4],", глупые смерти =",stats[5])

        print("Вы прилетели в Сидней на The International")
        i=0
        count = 0

        for i in range(len(stats)):
            count += stats[i]
            i+=1
        
        count -=stats[5]
        count -=stats[5]
        if count > 37:
            print("Вы спокойно доходте до полу-финала")
        
        random.randint(1,5)
        if random == 5:
            TeamMood -=20
            print("К сожалению игрок твоей команды нарушил правила турнира и был выгнан с турнира")
            choice = int(input("Введите 1 чтобы найти замену игрока\n Введите 2 чтобы просто получить тех. поражение"))
            if choice == 1 and TeamMood<40:
                print("Вы упороно боролись, но из-за того что у вас была замена вы проиграли")
        else:
            print("В полу-финале вы играете с Team Liquid и в кровожадной борьбе на 88 минуте сносите трон и попадаете в финал")
            
            print("В финале вы попали на Gaiming Gladiatros")
            miss = 0
            print("Вы пикаете персонажей.")
            pick = input("У вас будет метовый пик или нет?")
            if pick != "метовый":
                miss+=1
            
            choice = ("Ты стоишь на выиграном лайне и фрамишь. Будешь фармит на своей территории?(да/нет)")
            if choice == "нет":
                miss+=1

            choice=int(input("Происходит файт в котором мало шаносв на успех что ты будешь делать? (1. Использую тп на базу. 2. Останусь и буду драться(только цифру))"))
            if choice == 2:
                miss+=1

            if miss == 3:
                print("Вы без шансов проиграли финал. Вы разочаровали зрителей")
                TeamMood -=20

            if miss<2:
                print("Вы очень круто сыграли и побеили")
            
            


           
    except :
        print("Invalid input")

if player == 2:
    try:
        TeamMood = random.randint(60,100)
        print("Вы выбрали своего игрока")
        Name = input("Введите имя ")
        Surname = input("Введите фамилию ")
        Nick = input("Введите ник ")
        team = teams[random.randint(0, 4)]
        print("Ваш игрок {} {} {}".format(Name,Nick, Surname))
        stats = [random.randint(6,8), random.randint(6,8), random.randint(6,8), random.randint(6,8), random.randint(6,8), random.randint(1,4)]
    except:
        print("Invalid input") 

    
    YourTeam = input("Введите название вашей комнады ")

    print ("Вы зарегестрировались на квалификации к The International")
    print("Вы будете играть несколько матчей на квалификации")
    print("У вашей команды настрой на ", TeamMood, "баллов")
    wins = 0 
        
    i=1
    loses = 0
    while i< 3 and loses <2:
            print(i, " матч")
            if random.randint(1,10) >3:
                print("Вы выиграли ",i,"игру и идете дальше")
                wins+=1
                TeamMood+=5
            else:
                print("вы проиграли")
                TeamMood-=5
                loses+=1
            i+=1
    if wins > 2:
            print("Вы квалифицировались!!!")
  
    kruto = input("круто?")
       
    print("Теперь нужно немного отдохнуть!")
    
    print("После отдыха вы чуток потеряли форму\n"
            "чтобы вернуть форму надо потренить")
    trenyamb = input("Будешь тренироваться(да\нет)")
    if trenyamb == "да":
            
            print("Умничка")
    else:
           
            print("Ваш скил ухудшился")

    print("Вы прилетели в Сидней на The International")
    print("Скоро начнутьс матчи" )
        
    trenyamb = input("Будешь тренироваться(да\нет)")

    if trenyamb == "да":
            
            print("Умничка")
    else:
            print("Дурачок")

    print("Будет всего 2 игры. Все 2 выиграешь => ты чемпион")
    
    count =0
    for i in range(5):
                count += stats[i]
                i+=1
        
    if count > 35 and TeamMood > 70:
            print("1ую игру вы выиграли, осталось еще 2")
    
            print("анлак вы отлетели")
            money = 203412
            print("Вот твои призовые ", money)
    elif count > 45 and TeamMood > 75:
            print("2ую игру вы выиграли, осталось еще 1")
    

    elif count > 45 and TeamMood > 85:
            print("Бравоооооооо. Ты чемпион The International")
            input("К вам подоходит журналист и спрашивает как вам удлось выиграть")
            print("Не многим удавалось выиграть TI")
            money = 2574271
            print("Вот твои призовые ", money)
            
    else:
            print("анлак вы отлетели. Это обидно что вы проиграли в финале")
            money = 684556
            print("Вот твои призовые ", money)
   
else:
    print("ну ты совсем что-ли. сказано 1 или 2")