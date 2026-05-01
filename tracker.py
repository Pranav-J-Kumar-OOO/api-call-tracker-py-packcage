import requests
class tracker:
    def __init__(self,userid,passwd,p_id):
        self.userId=userid
        self.passWd=passwd
        self.projId=p_id

    def track(self, objId):
        params = {
            'userId': self.userId,
            'projectId': self.projId,
            'idname': objId
        }

        response = requests.get("https://api-call-tracker-production.up.railway.app/track", params=params)
        return (f"Status Code: {response.status_code}"+f"Response: {response.text}")
