from fastapi import APIRouter

router = APIRouter(prefix="/s3", tags=["s3"])

## Path params
@router.get("/{bucket}/{path}")
async def get_search(bucket:str, path: str):
    pass
    return {"need to perform s3 fetch here"}

