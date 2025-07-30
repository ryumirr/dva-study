[클라이언트-1]

Authorization: Bearer <JWT> 헤더와 함께
→ API Gateway (JWT 인증) 호출
→ Lambda (test-7-30) → Presigned URL 응답

[클라이언트-2]

받은 URL로 S3에 직접 업로드

[S3]

ObjectCreated:Put 이벤트 발생
→ Lambda(process-uploaded-image) 트리거

[Lambda (후처리)]

성공 시 / 실패 시 → SNS 알람 (이메일 전송)