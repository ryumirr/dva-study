**이벤트 기반 아키텍처(Event-driven architecture, EDA)**는 AWS Lambda 같은 서버리스 환경에서 아주 핵심적인 설계 패턴

이벤트 기반 아키텍처란?
"어떤 이벤트(event)가 발생하면, 그것을 감지하고 자동으로 반응(처리)하는 구조"
→ 이벤트에 의해 동작이 시작됨
ex) Kafka


[사용자가 이미지를 S3에 업로드]
          ↓ (이벤트)
    [S3: ObjectCreated 이벤트 발생]
          ↓
[Lambda가 자동으로 트리거됨]
          ↓
[Lambda가 썸네일 생성, DynamoDB에 기록]




## Lambda 튜닝 요약

메모리 조절: 메모리↑ → CPU↑ → 속도↑ (비용과 균형 조절)

패키지 최소화: 코드와 라이브러리 작게

Cold Start 줄이기: Layer 사용, VPC 피하기, Provisioned Concurrency
    + 콜드 스타트란?
    Lambda 함수가 오랫동안 실행되지 않다가 처음 실행될 때, AWS가 내부적으로 실행 환경을 새로 만드는 시간 지연
    = Lambda가 처음 실행될 때 환경을 준비하느라 느려지는 현상

* Lambda는 함수 실행 시 다음을 준비함:

가상 머신(컨테이너) 생성

메모리/코드 로딩

언어 런타임(Java, Python 등) 초기화

핸들러 함수 호출

→ 이 과정이 몇 백 ms ~ 몇 초 걸려서 느려짐



지연 로딩: 필요할 때 객체 생성

병렬 처리: 큰 작업은 쪼개서 여러 Lambda로

로깅 최소화: 너무 많은 로그는 성능 저하

타임아웃 조절: 적당한 실행 시간 설정



## 코드를 사용하여 이벤트 수명 주기 및 오류 처리(예: Lambda Destinations, 배달한 편지 대기열) 

이벤트 수명 주기	Lambda가 언제 시작되고, 어떻게 끝나며, 실패했을 때 어떤 일이 일어나는지를 추적

오류 처리	실패한 이벤트를 무시하지 않고 재시도, 저장, 알림 처리하는 구조

Lambda Destinations	Lambda가 성공 또는 실패한 후, 결과를 다른 서비스(SQS, SNS 등)에 자동 전달

Dead Letter Queue (DLQ)	Lambda가 반복 실패할 때, 이벤트를 저장해두는 백업 큐

