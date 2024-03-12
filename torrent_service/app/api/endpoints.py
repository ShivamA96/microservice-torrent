from fastapi import APIRouter, Depends
from fastapi import FastAPI, File, UploadFile, Form
router = APIRouter()
from prisma import Client

async def get_db():
    db = Client()
    await db.connect()
    try:
        yield db
    finally:
        await db.disconnect()

@router.get("/")
def read_root():
    return {"message": "Welcome to the Torrent Service"}

@router.post("/torrents")
async def create_torrent(db: Client = Depends(get_db), File: UploadFile = File(...)):

    if not File.filename:
        raise HTTPException(status_code=400, detail="File is required")

    with open(f"static/{File.filename}", "wb") as buffer:
        contents = await File.read()
        buffer.write(contents)

    torrent = await db.torrent.create({
        "title": File.filename,
        "path": f"static/{File.filename}",
        "description": "Dummy description",
        "uploaderId": "dummyUploaderId",
        "size": 123.45,
        "category": "Dummy category",
        "type": "Dummy type",
        "downloads": 0,
        "health": 100.0,  
    })

    return {"message": "Torrent created successfully", "torrent": torrent}
    
# @router.get("/torrents")
# def get_torrents():
#     # TODO: Implement logic to retrieve all torrents
#     return {"message": "Get all torrents"}


# @router.get("/torrents/{torrent_id}")
# def get_torrent(torrent_id: int):
#     # TODO: Implement logic to retrieve a specific torrent by ID
#     return {"message": f"Get torrent with ID {torrent_id}"}


# @router.post("/torrents")
# def create_torrent():

    

#     return {"message": "Create a new torrent"}


# @router.put("/torrents/{torrent_id}")
# def update_torrent(torrent_id: int):
#     # TODO: Implement logic to update a specific torrent by ID
#     return {"message": f"Update torrent with ID {torrent_id}"}


# @router.delete("/torrents/{torrent_id}")
# def delete_torrent(torrent_id: int):
#     # TODO: Implement logic to delete a specific torrent by ID
#     return {"message": f"Delete torrent with ID {torrent_id}"}


# @router.get("/torrents/{torrent_id}")
# def get_torrent(torrent_id: int):
#     # TODO: Implement logic to retrieve a specific torrent by ID