#8. (과제 3) 바둑판
### 입력 및 변수 선언
#바둑판
go = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 1, 0, 1, 2, 1, 2, 1, 0],
       [0, 2, 1, 1, 1, 2, 2, 0, 0],
       [0, 0, 2, 2, 2, 1, 0, 2, 0],
       [0, 0, 0, 0, 0, 1, 0, 2, 1],
       [0, 0, 0, 2, 0, 1, 2, 1, 0],
       [0, 0, 0, 2, 1, 0, 1, 1, 0],
       [0, 0, 0, 1, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 2, 2, 2, 0, 0]]

black = 0  # 흑돌 갯수 변수
white = 0  # 백돌 갯수 변수

### 1) 돌 개수 세기
for i in range(len(go)):   
    black += go[i].count(1)  #흑돌 개수 카운트
    white += go[i].count(2)  #백돌 개수 카운트
print('***********************')  #돌 개수 출력
print(f'흑돌의 개수: {black}')
print(f'백돌의 개수: {white}')
print('***********************')

### 2) 바둑알 특수문자로 변경하기
for i in range(len(go)):   
    for j in range(len(go[i])):
        if(go[i][j]==0):  #0이면..
            go[i][j]= '▒'
        elif(go[i][j]==1):  #1이면..
            go[i][j]= '●'
        elif(go[i][j]==2):  #2이면..
            go[i][j]= '○'
print('바둑알을 특수문자로 바꿔보자!(흑돌:●, 백돌:○, 돌 없음:▒)')
for i in go:  #출력 코드
    for j in i:
        print(f'{j}', end='') #공백 생성
    print()
print('***********************')

### 3) 어떤 좌표에 돌이 있는지 출력하기
while(True):  #무한루프
    x = int(input('X축 좌표값을 입력하세요(1~9, 종료시 -1 입력): '))
    if(x==-1):
        print('종료되었습니다!')
        break  #종료문
    y = int(input('Y축 좌표값을 입력하세요(1~9, 종료시 -1 입력): '))
    if(go[y-1][x-1]=='▒'):  
        print('돌없음')
        continue
    elif(go[y-1][x-1]=='●'):
        print('흑돌')
        continue
    elif(go[y-1][x-1]=='○'):
        print('백돌')
        continue

    