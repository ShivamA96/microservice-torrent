from fastapi import APIRouter, Depends
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.exceptions import HTTPException
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
async def create_torrent(db: Client = Depends(get_db), File: UploadFile = File(...), body: dict = Form(...)):

    if not File.filename:
        raise HTTPException(status_code=400, detail="File is required")

    with open(f"static/{File.filename}", "wb") as buffer:
        contents = await File.read()
        buffer.write(contents)

    torrent = await db.torrent.create({
        "title": File.filename,
        "path": f"static/{File.filename}",
        "description": body["description"],
        "uploaderId": "dummyUploaderId",
        "size": body["size"],
        "category": body["category"],
        "type": body["type"],
        "downloads": 0,
        "health": 100.0,  
    })

    return {"message": "Torrent created successfully", "torrent": torrent}
    
@router.get("/torrents")
def get_torrents(db: Client = Depends(get_db)):
    # TODO: Implement logic to retrieve all torrents
    torrents = db.torrent.findMany()

    if not torrents:
        raise HTTPException(status_code=404, detail="No torrents found")
    return {"Torrents": torrents}



@router.get("/torrents/{torrent_id}")
async def get_torrent(torrent_id: int, db: Client = Depends(get_db)):
    torrent = await db.torrent.find_unique(where={"id": torrent_id})
    if not torrent:
        raise HTTPException(status_code=404, detail="Torrent not found")
    return {"Torrent": torrent}

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