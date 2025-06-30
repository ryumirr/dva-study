#!/bin/bash

# 날짜 설정
DATE=$(date +%F)

# S3 정보
BUCKET="my-readonly-bucket"
KEY="backups/daily.zip"
DEST="/home/backup/daily-$DATE.zip"

# 읽기 전용 사용자 프로파일
PROFILE="readonly-user"

# S3에서 파일 다운로드
aws s3 cp s3://$BUCKET/$KEY $DEST \
  --region ap-northeast-1 \
  --profile $PROFILE