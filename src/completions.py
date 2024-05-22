import boto3
import json

AWS_REGION = 'us-east-1'

# Amazon Bedrock Runtime is the API entry endepoint for invoking foundational models
bedrock = boto3.client('bedrock-runtime',region_name=AWS_REGION)

# helper function called get_c3_completion that sends a prompt to Claude and returns the generated response
def get_c3_completion(messages,
                      modelId = 'anthropic.claude-3-haiku-20240307-v1:0',
                      system = '',
                      max_tokens = 2000,
                      top_p = 1,
                      top_k = 50,
                      temperature = 0,
                      stop_sequences = ['Human: ']):
    body = json.dumps(
        {
            "anthropic_version": '',
            "messages": messages,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "top_k": top_k,
            "temperature": temperature,
            "system": system,
            "stop_sequences": stop_sequences
        }
    )
    response = bedrock.invoke_model(body=body, modelId=modelId)
    response_body = json.loads(response.get('body').read())

    return response_body.get('content')[0].get('text')

# helper function called get_mistral_completion that sends a prompt to Mistral and returns the generated response
def get_mistral_completion(prompt,
                           modelId = 'mistral.mistral-7b-instruct-v0:2',
                           max_tokens = 2000,
                           top_p = 1,
                           top_k = 50,
                           temperature = 0): 

    body = json.dumps({ 
        'prompt': prompt,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "top_k": top_k,
        "temperature": temperature,
        "stop": ["</s>"]
    })

    try:
        response = bedrock.invoke_model(body=body, modelId=modelId)
        response_body = json.loads(response.get('body').read().decode('utf-8'))
        outputs = response_body["outputs"]
        outputText = [output["text"] for output in outputs]
        return outputText[0]

    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'AccessDeniedException':
            return (f"\x1b[41m{error.response['Error']['Message']}\
                    \nTo troubleshoot this issue please refer to the following resources.\
                     \nhttps://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_access-denied.html\
                     \nhttps://docs.aws.amazon.com/bedrock/latest/userguide/security-iam.html\x1b[0m\n")
        else:
            raise