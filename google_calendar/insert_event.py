from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

#----------------ここがイベント追加コード始まり-----------------------
    event = {
        'summary': '習慣サンプル1',
        'description': 'サンプルの予定',
        'start': {
        'dateTime': '2020-12-12T09:00:00',
        'timeZone': 'Japan',
        },
        'end': {
        'dateTime': '2020-12-12T17:00:00',
        'timeZone': 'Japan',
        },
    }
#----------------ここがイベント追加コード終わり-----------------------

    event = service.events().insert(calendarId='r3vsm0ul313e2bj0k8u4selfvo@group.calendar.google.com',
                                    body=event).execute()
    print (event['id'])

if __name__ == '__main__':
    main()