import boto3
import json

bedrock=boto3.client(service_name="bedrock-runtime")
payload ={
    "prompt":"[INST] You are an economist with access to lots of data [/INST] Write an article about impact of high inflation to GDP of a country",
    "max_gen_len":512,
    "temperature":0.5,
    "top_p":0.9
}
body=json.dumps(payload)
model_id="meta.llama2-70b-chat-v1"


response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json"
)

response_body=json.loads(response.get("body").read())

response_text=response_body['generation']
print(response_text)
