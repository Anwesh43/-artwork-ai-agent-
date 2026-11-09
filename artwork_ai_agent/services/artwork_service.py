from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 

load_dotenv()

class ArtworkService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["ARTWORK_BASE_URL"]) 
        self.headers = {
            "AIC-User-Agent": os.environ["AIC_USER_AGENT"],
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:159.0) Gecko/20100101 Firefox/159.0"
        }

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
            response = self.client.getCall("artworks", qpParams = qpParams, headers = self.headers)
            return response["data"]
        except Exception as e:
            return self._handleError(e)

    def getArtworkDetails(self, artworkId : str):
        try:
            response = self.client.getCall(f"artworks/{artworkId}", headers = self.headers)
            return response
        except Exception as e:
            return self._handleError(e)


    def searchArtwork(self, query : str):
        try:
            response = self.client.getCall(f"artworks/search", qpParams={"q", query}, headers = self.headers)
            return response["data"] 
        except Exception as e:
            return self._handleError(e)

    def getExhibitions(self):
        try:
            qpParams = {
                "fields": "id,title"
            }
            response = self.client.getCall(f"exhibitions", qpParams=qpParams, headers = self.headers)
            return response["data"]
        except Exception as e:
            return self._handleError(e)

    def getExhibitionDetails(self, exhibitionId : str):
        try:
            response = self.client.getCall(f"exhibitions/{exhibitionId}", headers = self.headers)
            return response
        except Exception as e:
            return self._handleError(e)

    def getGalleries(self):
        try: 
            qpParams = {
                "fields": "id,title"
            }
            response = self.client.getCall(f"galleries", qpParams=qpParams, headers = self.headers)
            return response["data"]
        except Exception as e:
            return self._handleError(e)

    def getGalleryDetails(self, galleryId : str):
        try:
            response = self.client.getCall(f"galleries/{galleryId}", headers = self.headers)
            return response
        except Exception as e:
            return self._handleError(e)

    def getPlaces(self):
        try:
            qpParams = {
                "fields": "id,title" 
            }
            response = self.client.getCall(f"places", qpParams = qpParams, headers = self.headers)
            return response["data"]
        except Exception as e:
            return self._handleError(e)

    def getPlaceDetails(self, placeId : str):
        try:
            response = self.client.getCall(f"places/{placeId}", headers= self.headers)
            return response 
        except Exception as e:
            return self._handleError(e)
        