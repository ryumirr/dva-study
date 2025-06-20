from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_s3_deployment as s3deploy,
)
from constructs import Construct
from pathlib import Path


class LambdaS3Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Lambda 실행 권한 Role 생성
        lambda_role = iam.Role(
            self,
            "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AWSLambdaBasicExecutionRole"
                )
            ],
        )

        # S3 버킷 생성 (버전 관리 활성화)
        bucket = s3.Bucket(
            self,
            "S3Bucket1",
            versioned=True
        )

        # Lambda 함수 생성
        my_lambda = _lambda.Function(
            self,
            "MyLambdaFunction",
            function_name="MyS3TriggerFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.lambda_handler",
            role=lambda_role,
            code=_lambda.Code.from_inline(
                '''import json
import datetime

def lambda_handler(event, context):
    current_time = datetime.datetime.utcnow().isoformat()
    print("Event received:", event)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello from Lambda :X",
            "time": current_time
        })
    }
'''
            ),
        )

        # S3 → Lambda 트리거 연결
        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(my_lambda)
        )

        # Lambda가 S3 버킷 읽을 수 있도록 권한 부여
        bucket.grant_read(my_lambda)

        # 초기 파일 S3에 배포 (upload-folder/에 업로드됨)
        s3deploy.BucketDeployment(
            self,
            "DeploySampleFile",
            sources=[s3deploy.Source.asset(
                str(Path(__file__).parent / "sample-data")
            )],
            destination_bucket=bucket,
            destination_key_prefix="upload-folder/"
        )