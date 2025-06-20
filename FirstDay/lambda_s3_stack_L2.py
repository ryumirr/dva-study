from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
)
from constructs import Construct

class LambdaS3Stack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        # S3 버킷 생성
        # CDK 코드 내부에서 어떤 추상화 수준의 Construct를 사용했느냐에 따라 L1,L2,L3가 나눠짐
        # bucket = s3.Bucket(self, "S3Bucket1") #L2-1
        bucket = s3.Bucket(self, "S3Bucket1",
                        versioned=True) #L2-2

        # Lambda 함수 생성
        my_lambda = _lambda.Function(
            self,
            "MyLambdaFunction",
            function_name="MyS3TriggerFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.lambda_handler",
            role=lambda_role,
            # Function Invoke용(커맨드 사용시에만 로그남음)
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
'''),)
        # S3 이벤트 알림에 Lambda 연결
        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(my_lambda)
        )

        # Lambda가 S3 읽기 권한을 가지도록 설정
        bucket.grant_read(my_lambda)