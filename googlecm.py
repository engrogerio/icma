import google_auth

def get_user_profiles(service): #, **kwargs):
    results = service.userProfiles().list().execute()
    print(results['items'])
    return results
