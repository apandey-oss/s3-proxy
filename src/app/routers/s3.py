from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from app import config
from boto3 import client as boto3_client
from botocore.exceptions import ClientError

# import mimetypes

router = APIRouter()


## Path params
@router.get("/{bucket}/{path:path}")
async def get_search(bucket: str, path: str):
    try:
        c = boto3_client('s3', aws_access_key_id=config.access_key, aws_secret_access_key=config.secret_key)
        content = c.get_object(Bucket=bucket, Key=path)
        return Response(content=content['Body'].read(), media_type=content['ContentType'])
    except ClientError:
        return JSONResponse(
            status_code=404, content={"message": f"Not found or other error occured"}
        )
