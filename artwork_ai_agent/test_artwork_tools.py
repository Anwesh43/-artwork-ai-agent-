from tools.artwork_tools import getArtworkDetails, getArtworks, searchArtwork, getPlaceDetails, getPlaces, getGalleries, getGalleryDetails, getExhibitions, getExhibitionDetails, getImage 
from typing import Dict 
import json 

def writeFile(fileName : str, data : Dict):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Writing data to {fileName}")

if __name__ == "__main__":
    places = getPlaces()
    writeFile("test_places.json", places)
    if len(places) > 0 and "id" in places[0]:
        placeId = places[0]["id"]
        writeFile(f"test_places_{placeId}.json", getPlaceDetails(placeId))
    galleries = getGalleries()
    writeFile("test_galleries.json", galleries)
    if len(galleries) > 0 and "id" in galleries[0]:
        galleryId = galleries[0]["id"]
        writeFile(f"test_gallery_{galleryId}.json", getGalleryDetails(galleryId))
    artworks = getArtworks()
    writeFile("test_artworks.json", artworks)
    if len(artworks) > 0 and "id" in artworks[0]:
        artworkId = artworks[0]["id"]
        writeFile(f"test_artwork_{artworkId}.json", getArtworkDetails(artworkId=artworkId))
    exhibitions = getExhibitions()
    writeFile("test_exhibitions.json", exhibitions)
    if len(exhibitions) > 0 and "id" in exhibitions[0]:
        exhibitionId = exhibitions[0]["id"]
        writeFile(f"test_exhibition_{exhibitionId}.json", getExhibitionDetails(exhibitionId=exhibitionId))

    writeFile("test_image_details.json", getImage(" https://www.artic.edu/iiif/2/e8e67721-bbb1-d007-82bd-c430ea73db70"))
    