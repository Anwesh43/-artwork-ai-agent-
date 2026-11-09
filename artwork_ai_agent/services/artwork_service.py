from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 

load_dotenv()

class ArtworkService:
    def __init__(self, baseURL : str):
        self.client = BaseHTTPClient(baseURL) 

    def _handleError(self, e):
        print("Error", str(e))
        return {
            "status": "Error",
            "message": str(e)
        }
    
    def getArtworks(self):
        try:
            qpParams = {
                "fields": "id,title"
            }
            response = self.client.getCall("artworks", qpParams = qpParams)
            return response["data"]
        except Exception as e:
            return self._handleError(e)

    def getArtworkDetails(self, artworkId : str):
        try:
            response = self.client.getCall(f"artworks/{artworkId}")
            return response
        except Exception as e:
            return self._handleError(e)


    def sarchArtwork(self, query : str):
        try:
            response = self.client.getCall(f"artworks/search", qpParams={"q", query})
            return response["data"] 
        except Exception as e:
            return self._handleError(e)

    def getExhibitions(self):
        try:
            qpParams = {
                "fields": "id,title"
            }
            response = self.client.getCall(f"exhibitions", qpParams=qpParams)
            return response["data"]
        except Exception as e:
            return self._handleError(e)

    def getExhibitionDetails(self, exhibitionId : str):
        try:
            response = self.client.getCall(f"exhibitions/{exhibitionId}")
            return response
        except Exception as e:
            return self._handleError(e)

    def getGalleries(self):
        try: 
            qpParams = {
                "fields": "id,title"
            }
            response = self.client.getCall(f"galleries", qpParams=qpParams)
            return response["data"]
        except Exception as e:
            return self._handleError(e)

    def getGalleryDetails(self, id : str):
        try:
            response = self.client.getCall(f"galleries/{id}")
            return response
        except Exception as e:
            return self._handleError(e)

    def getPlaces(self):
        try:
            qpParams = {
                "fields": "id,title" 
            }
            response = self.client.getCall(f"places", qpParams = qpParams)
            return response 
        except Exception as e:
            return self._handleError(e)

    def getPlaceDetails(self, placeId : str):
        try:
            response = self.client.getCall(f"places/{placeId}")
            return response 
        except Exception as e:
            return self._handleError(e)
        