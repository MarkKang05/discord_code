# 민트봇 
### (민트처리 및 온라인 수업 관련 데이터 제공)

민트봇은 온라인 수업 때 항상 선생님 줌코드가 적힌 엑셀을 봐야하는 귀찮니즘을 해결하기 위하여 만들어지 디스코드 메신저 봇입니다.
![discord](https://user-images.githubusercontent.com/47387289/155095734-a773ca4b-d682-43df-accf-3c68186a7d7b.png)


### 동작 과정
기본적인 통신은 토큰을 발급받아 discord.py 라이브러리를 사용하며, 서비스 단만 개발하였습니다. 

*데이터 베이스*  (연관관계 설정 x)
(개발 당시 데이터 베이스 지식이 부족했기 때문에 때문에 연관관계 설정은 안함.)
![Screen Shot 2022-02-22 at 5 18 17 PM](https://user-images.githubusercontent.com/47387289/155096094-dc6be14c-21a4-4929-8946-551a900275ca.png)
![Screen Shot 2022-02-22 at 5 18 37 PM](https://user-images.githubusercontent.com/47387289/155096153-23e9f54a-f9e6-40a3-a005-7efdc5a1400a.png)

``` sql
SELECT period, A.name AS class_name, A.z_code FROM class_time B
  INNER JOIN class A
   ON B.code = A.code
WHERE WEEK = '2'
ORDER BY WEEK, period, B.code;
``` from lib/maria_python.py

*서비스*
* 수업 줌 코드 출력
![discord](https://user-images.githubusercontent.com/47387289/155095734-a773ca4b-d682-43df-accf-3c68186a7d7b.png)
* 날씨 출력(지역 입력 후)
![ weather](https://user-images.githubusercontent.com/47387289/155097941-d32c2a6f-4604-468b-914f-9906ea5addbc.png)
* 코로나 확진자 수 
![corona](https://user-images.githubusercontent.com/47387289/155098368-980560b6-237e-4ba8-a2f1-1610576d6594.png)
* 민트 검열 및 삭제 & 민트 도배 시 경고 메세지
![mint](https://user-images.githubusercontent.com/47387289/155098741-37485220-067f-480a-9acb-fd5021ef5a8b.png)
* 기타


*배포*
저전력으로 24시간 운영을 해야하기 때문에 라즈베리파이를 서버로 사용했습니다.
관리의 편의를 위해 컨테이너화 하여 도커를 이용하여 관리. 
![Screen Shot 2022-02-22 at 5 25 59 PM](https://user-images.githubusercontent.com/47387289/155096483-188ebfd3-19d1-449e-bcb3-399dd2b01a6e.png)

*기타*
git과 도커를 사용하니, 중간에 라즈베리파이를 업그레이드 할때가 있었는데 정말 말도 안되게 쉽게 재배포 가능했습니다(혹시라도 라즈베리파이가 재부팅 되더라도 도커에서 자동으로 컨테이너도 재시작)


~~패밀리 서비스~~
아잉봇 <https://github.com/MarkKang05/aingbot>
