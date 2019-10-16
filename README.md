# 프로젝트

* Kakao OpenBuilder를 사용해 Kakao 플러스 친구 생성
* Kakao에서 Django Server로 가상화폐 이름, 거래소 를 전달
* 전달받은 가상화폐 이름 , 선택한 거래소의 open api를 사용해 데이터를 받아옴
* 전달받은 데이터를 Kakao로 Response해 답글 생성

# 담당

* Kakao OpenBuilder를 신청해 Kakao 플러스 친구 생성
* Django를 사용해 서버 구축
* 거래소의 Open API 를 사용해 해당 가상화폐의 데이터를 전달받음
* uwsgi , nginx를 Django와 연동
* AWS EC2를 사용해 배포


### Stack

* Django
* 각 거래소 Open API
* Uwsgi
* Nginx
* AWS EC2
* Kakao API


# 첨부

### Github

* https://github.com/hckcksrl/coin_chat

### 플러스 친구

* 플러스친구 : http://pf.kakao.com/_VfxoWT
