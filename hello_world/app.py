import json

from uuid import uuid4

import boto3



def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource("dynamodb")

        table =  dynamodb.Table("Sneakers")


        body =  json.loads(event['body'])


        if 'model' not in body or body['model'] is None or body['model'] == "":
            raise Exception("O Campo model deve estar preenchido")
        

        if 'brand' not in body or body['brand'] is None or body['brand'] == "":
            raise Exception("O Campo brand deve estar preenchido ")
        

        if body['year'] is None:
            raise Exception("O Campo year deve estar preenchido ")
        

        id_unico = uuid4()
        payload_db =  {
            "id": str(id_unico),
            "model": body['model'],
            "brand": body['brand'],
            "url_img": body['url_img'] if "url_img" in body else ""
        }

        table.put_item(
           Item=payload_db
        )
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "hello world"
            }),
        }
    except Exception as e:
        print(e)

        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": f"Erro: {e} "
            })
        }
        
