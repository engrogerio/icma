"""
IProspect Campaign Manager Automation
"""
import googlecm as gcm
import google_auth as auth

class icma:
    def __init__(self, account=None, campaign=None):
        self.account = account
        self.campaign = campaign
        self.service = auth.get_authenticated_service()
        self.profiles = gcm.get_user_profiles(self.service)

