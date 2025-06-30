
# AWS IAM + Security Domain 2 - Task 1 실습 가이드

---

## ✅ Stage 1: IAM 기초 개념 및 실습

### 실습: IAM 사용자 생성 → S3에 Read-only 접근 정책 연결 → 테스트

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::my-bucket-name/*"
    }
  ]
}
```

---

## ✅ Stage 2: 인증 메커니즘 이해와 실습

### 실습: IAM Role과 STS를 이용한 cross-account access 구현

```json
{
  "Effect": "Allow",
  "Principal": {
    "AWS": "arn:aws:iam::<B_ACCOUNT_ID>:root"
  },
  "Action": "sts:AssumeRole"
}
```


## ✅ Stage 3: 사용자 인증 및 ID 페더레이션

### 실습: Google 계정으로 로그인 후 Cognito + IAM 연동

1. **Cognito 사용자 풀 만들기**
   - Amazon Cognito → Create user pool
     - Add user sign-in (username/email)
     - Enable hosted UI

2. **자격 증명 풀로 IAM 역할 연결**
   - Cognito → Federated Identities → Create identity pool
     - Enable access to unauthenticated identities
   - IAM 역할 연결:
     - 자격 증명 풀에 연결된 역할에 S3 정책 추가

3. **외부 ID (Google) 연동**

---

## ✅ Stage 4: 권한 부여 및 정책 제어 실습

### 실습: S3 버킷에 리소스 기반 정책 적용 + IAM 사용자 그룹으로 제어

```json
{
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::my-public-bucket/*"
}
```

---

## 🔜 아직 미실습

### ⏳ RBAC 그룹 권한 실습
- IAM → Groups → Create group (예: `AdminGroup`)
- 정책 연결: 예) `AmazonEC2FullAccess`
- IAM 사용자 그룹에 추가하여 권한 부여


-------------------


## 실습1

## ✅ Verify S3 access for the user named 'nini' after configuring the new IAM role and user profile on aws CLI

```bash
aws configure --profile nini

aws configure list --profile nini

cat ~/.aws/config

aws s3 ls --profile nini

aws sts assume-role \
  --role-arn arn:aws:iam::{account-id}:role/s3-add-role-name \
  --role-session-name demoSession \
  --profile nini
```

---

## ✅ Use MFA with the AWS CLI

```bash
aws sts get-session-token \
  --serial-number arn:aws:iam::{account-id}:mfa/nini \
  --token-code 749947 \
  --profile nini

aws sts get-session-token
```

---

## 실습2

### S3 Read-only User Restricted to Specific IP (localhost backup)

`SecondDay/cloudFormation.yaml`

`SecondDay/s3-backup.sh`

----

aws cloudformation create-stack \
  --stack-name backup-s3-ip-restricted \
  --template-body file://SecondDay/cloudFormation.yaml \
  --parameters ParameterKey=AllowedIP,ParameterValue=203.0.113.25/32 \
  --capabilities CAPABILITY_NAMED_IAM