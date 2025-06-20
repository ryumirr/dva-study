# dva-study

[First day]

cdk deploy --app "python app.py" --region us-east-1

aws lambda invoke \                                     ─╯
  --function-name MyS3TriggerFunction \
  --payload '{}' \
  --region us-east-1 \
  output.json