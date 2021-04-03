# https://github.com/googleapis/google-api-python-client/blob/master/docs/oauth-installed.md
import os
import google.oauth2.credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"


# When running locally, disable OAuthlib's HTTPs verification. When
# running in production *do not* leave this option enabled.
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '0'

# This access scope grants read-only access to the authenticated user's Drive
# account.
SCOPES = ["https://www.googleapis.com/auth/dfareporting", "https://www.googleapis.com/auth/dfatrafficking"]
API_SERVICE_NAME = 'dfareporting'
API_VERSION = 'v3.4'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
