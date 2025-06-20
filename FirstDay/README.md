# dva-study

## First day 실습 요약

---

### ✅ [L2 - CloudFormation + CLI 방식]

```bash
# CDK 환경 준비
cdk bootstrap aws://<account-id>/us-east-1

# CloudFormation 템플릿 배포
aws cloudformation deploy \
  --template-file cloudFormation/cloudFormation.yaml \
  --stack-name Larav3 \
  --capabilities CAPABILITY_IAM

# Lambda 수동 호출
aws lambda invoke \
  --function-name MyS3TriggerFunction \
  --payload '{}' \
  --region us-east-1 \
  FirstDay/output.json



### ✅ L3 + L2 - CDK 방식]

# CDK 스택 배포 (app.py에서 lambda_s3_stack_L3.py 사용)
cdk deploy --app "python FirstDay/app.py" --region us-east-1


### 프로젝트 구성

| 파일명                            | 설명                                                                          |
| ------------------------------ | --------------------------------------------------------------------------- |
| `lambda_s3_stack_L3.py`        | CDK (Python)으로 Lambda + S3 + IAM + S3Deploy 인프라 구성                          |
| `app.py`                       | CDK 앱 실행 진입점 (`app.synth()`로 CloudFormation 템플릿 생성)                         |
| `freetier-cloudFormation.yaml` | CloudFormation 템플릿 (S3 + Lambda Permission 설정) + `lambda_s3_stack_L2.py` 포함 |



### CDK vs SDK 언제 쓰는 게 좋을까?

| 목적                          | CDK (Infrastructure as Code)          | SDK (애플리케이션 코드에서 API 호출)   |
| --------------------------- | ------------------------------------- | -------------------------- |
| 리소스 생성/설정                   | ✅ 매우 적합 (예: S3, Lambda, DynamoDB 만들기) | ❌ 리소스 생성은 복잡하고 비효율적        |
| 리소스 업데이트/배포 자동화             | ✅ IaC로 선언적으로 처리                       | ❌ 직접 API 호출 반복 필요          |
| 코드 내에서 동작 (파일 업로드, 메일 전송 등) | ❌ 인프라 변경 도구일 뿐 실행 불가                  | ✅ 매우 적합 (boto3, aws-sdk 등) |
| Lambda 내부에서 AWS 서비스 호출      | ❌ 못함                                  | ✅ 적합 (S3에 업로드, SNS 전송 등)   |
| Terraform처럼 사용              | ✅ 가능 (CLI + IaC 형태)                   | ❌ 해당 아님                    |


