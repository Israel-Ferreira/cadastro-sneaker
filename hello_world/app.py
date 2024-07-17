import json
import logging

from base64 import b64decode
from requests_toolbelt.multipart import decoder





def get_filename_from_b64_decoded_str(b64_decoded_str):
    """
    Função copiada do artigo do Medium: https://fabaraujo23.medium.com/upload-de-xls-xlsx-utilizando-lambda-s3-python-e-localstack-ca653e0ff27b
    """

    logging.info(b64_decoded_str)

    filename_position =  b64_decoded_str.find("filename=\"")
    filename_complete_pos = b64_decoded_str.find("\"", filename_position + 10)

    filename = b64_decoded_str[filename_position+10:filename_complete_pos]

    print(filename)

    return filename



def validate_payload(multipart_form: decoder.MultipartDecoder):
    for part in multipart_form.parts:
        header_values = str(part.headers[b"Content-Disposition"]).split(";")
        print(header_values)


    





def upload_img_to_s3(filename, file_content, bucket_name):
    print(f"Nome do Arquivo: {filename}, Bucket: {bucket_name}")









def lambda_handler(event, context):
    try:
        b64_decoded =  b64decode(event['body']).decode("iso-8859-1")
        content_type =  event['headers']['Content-Type']

        str_b64_decoded = str(b64_decoded)

        filename_multipart =  get_filename_from_b64_decoded_str(str_b64_decoded)

        multipart_form = decoder.MultipartDecoder(b64_decoded.encode('utf-8'),content_type)

        validate_payload(multipart_form)
        

        img_bytes = bytes(multipart_form.parts[-1].text, encoding='utf8')

        upload_img_to_s3(filename_multipart,img_bytes, "TesteBuckets")

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
                "message": str(e)
            })
        }
        
