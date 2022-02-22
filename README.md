# 🚫 [민트처리봇](https://github.com/MarkKang05/discord_code)


# 1. 🤖 봇 소개
* 민트처리봇은 온라인 수업 때 항상 선생님 줌코드가 적힌 엑셀을 봐야하는 귀찮니즘을 해결하기 위하여 만들어진 디스코드 메신저 봇입니다.
* 민트와 관련된 단어를 모두 지워버립니다. 도배할 시, 경고 문자와 이미지가 랜덤으로 응답합니다.

<img src="https://user-images.githubusercontent.com/47387289/155095734-a773ca4b-d682-43df-accf-3c68186a7d7b.png" width="500"/>

---


# 2. 📚 기술 스택
* Python 3
* MySQL
* Docker


lib
* Discord.py 1.7.2
* BeautifulSoup
* Python-dotenv
* PyMySql

---


# 3. 💻 서비스 구현

* 수업 줌 코드 출력

<img src="https://user-images.githubusercontent.com/47387289/155095734-a773ca4b-d682-43df-accf-3c68186a7d7b.png" width="400"/>

* 날씨 출력(지역 입력 후)

<img src="https://user-images.githubusercontent.com/47387289/155097941-d32c2a6f-4604-468b-914f-9906ea5addbc.png" width="400"/>

* 코로나 확진자 수 

<img src="https://user-images.githubusercontent.com/47387289/155098368-980560b6-237e-4ba8-a2f1-1610576d6594.png" width="200"/>

* 민트 검열 및 삭제 & 민트 도배 시 경고 메세지

<img src="https://user-images.githubusercontent.com/47387289/155098741-37485220-067f-480a-9acb-fd5021ef5a8b.png" width="400"/>


* 데이터베이스
<img src="https://user-images.githubusercontent.com/47387289/155096094-dc6be14c-21a4-4929-8946-551a900275ca.png" width="440"/>
<img src="https://user-images.githubusercontent.com/47387289/155096153-23e9f54a-f9e6-40a3-a005-7efdc5a1400a.png" width="300"/>

* 요일별 과목/수업코드 조회
``` sql
SELECT period, A.name AS class_name, A.z_code FROM class_time B
  INNER JOIN class A
   ON B.code = A.code
WHERE WEEK = '2' //1: 월요일, 2: 화요일 ...
ORDER BY WEEK, period, B.code;
```
from [lib/maria_python.py](https://github.com/MarkKang05/discord_code/blob/master/lib/maria_python.py)


* discord API 토큰과 디스코드 멤버 고유번호(수업코드 반별 관리)를 위해 .env로 프로그램 내 환경변수 관리

 


---

# 4. 🛠 배포

* 저전력으로 24시간 운영을 해야하기 때문에 라즈베리파이를 서버로 사용.
* 관리의 편의를 위해 컨테이너화 하여 도커를 이용하여 관리. 
    * [Dokerfile](https://github.com/MarkKang05/discord_code/blob/master/Dockerfile)
    * [docker-compose.yml](https://github.com/MarkKang05/discord_code/blob/master/docker-compose.yml)
<img src="https://user-images.githubusercontent.com/47387289/155096483-188ebfd3-19d1-449e-bcb3-399dd2b01a6e.png" width="700"/>


* git과 도커를 사용하니, 중간에 라즈베리파이를 업그레이드 할때가 있었는데 매우 간편하게 재배포 가능했음
* (혹시라도 라즈베리파이가 재부팅 되더라도 도커에서 자동으로 컨테이너도 재시작)



---

👨‍👨‍👦 ~~패밀리 서비스~~

아잉봇 <https://github.com/MarkKang05/aingbot>
