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
        bucket = s3.Bucket(self, "S3Bucket1")

        # Lambda 함수 생성
        my_lambda = _lambda.Function(
            self,
            "MyLambdaFunction",
            function_name="MyS3TriggerFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.lambda_handler",
            role=lambda_role,
            code=_lambda.InlineCode(
                '''def lambda_handler(event, context):
    print("Event received:", event)
    return {"statusCode": 200, "body": "Hello from Lambda :X"}'''
            ),
        )

        # S3 이벤트 알림에 Lambda 연결
        bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(my_lambda)
        )

        # Lambda가 S3 읽기 권한을 가지도록 설정
        bucket.grant_read(my_lambda)
