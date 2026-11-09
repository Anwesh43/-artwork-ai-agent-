from services.artwork_service import ArtworkService 

artworkService = ArtworkService()

def getArtworks():
    print(f"Calling getArtworks tool")
    return artworkService.getArtworks()

def getArtworkDetails(artworkId : str):
    print(f"Calling getArtworkDetails {artworkId}")
    return artworkService.getArtworkDetails(artworkId=artworkId)

def getGalleries():
    print(f"Calling getGalleries tool")
    return artworkService.getGalleries()

def getGalleryDetails(galleryId : str):
    print(f"Calling getGalleryDetails for {galleryId}")
    return artworkService.getGalleryDetails(galleryId = galleryId)

def getExhibitions():
    print(f"Calling getExhibitions tool")
    return artworkService.getExhibitions()

def getExhibitionDetails(exhibitionId : str):
    print(f"Calling getExhibitionDetails tool for {exhibitionId}")
    return artworkService.getExhibitionDetails(exhibitionId=exhibitionId)

def searchArtwork(query : str):
    print(f"Calling searchArtwork tool call for {query}")
    return artworkService.searchArtwork(query=query)

def getPlaces():
    print(f"Calling getPlaces tool")
    return artworkService.getPlaces()

def getPlaceDetails(placeId : str):
    print(f"Calling getPlaceDetails tool for {placeId}")
    return artworkService.getPlaceDetails(placeId = placeId)

def getTools():
    tools = []
    tools.append(getArtworks)
    tools.append(getArtworkDetails)
    tools.append(getExhibitions)
    tools.append(getExhibitionDetails)
    tools.append(getGalleries)
    tools.append(getGalleryDetails)
    tools.append(searchArtwork)
    tools.append(getPlaceDetails)
    tools.append(getPlaces)
    return list(set(tools))
 