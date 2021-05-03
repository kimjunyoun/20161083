startdigimon = ['아구몬', '파닥몬', '메탈몬' ,'워그레이몬','홀리몬']	

def Menu():
    print(" 디지몬 월드에 오신 것을 환영합니다.")

    print("1. 시작하기")
    print("2. 종료하기")
    select = input("선택: ")
    return select

def Bab():
    dictselect= {'1': "밥을 먹다 배가 터져서 죽었습니다.:게임오버 ", '2': "굶어서 죽었습니다.: 게임오버", '3': "사냥을 하다 죽었습니다.:게임오버"}
    print("\n디지몬이 배고파 합니다. 어떻게 하시겠습니까?(숫자를 선택하세요)")
    print("1.밥을준다, 2. 굶긴다 3. 사냥을한다.")
    user_input = input() 
    print(dictselect[user_input])    

def PlayerName1():
    return input("플레이어의 이름을 정하세요 ")    

def Startdigimon1():
    index = 1
    for digimon in startdigimon:
        print(str(index) + '. ' + digimon)
        index += 1
    return input("디지몬을 선택해주세요 (이름으로 적어주세요) ")           

def Message(name, digimon):
    print ("플레이어의 이름은:" + name + "입니다.")
    print (digimon + "과 함께 디지몬 월드를 여행해보세요.")


def NewGame():
    playerName = PlayerName1()
    playerdigimon = Startdigimon1()
    Message(playerName, playerdigimon)
    
    

select = Menu()
if select == "1":
    NewGame()
elif select =="2":
    print("종료되었습니다.")  

Bab()


