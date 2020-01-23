import requests
import json


# Class to authenticate user to ledningskollen.
class APIRequests:

    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.authentication = ''
        self.session = ''
        # The (verification) token needs to be added to all POST-Request.
        self.token = ''
        self.header = ''
        self.status_message = ''

    def login(self):
        # Login to API creating an auth token
        try:
            # login = requests.post(self.base_url + "auth", auth=requests.auth.HTTPBasicAuth(self.username, self.password))
            payload = {'inUserName': self.username, 'inUserPass': self.password}
            login = requests.post(self.base_url + '/auth', auth=(self.username, self.password), allow_redirects=True,
                                  headers={'accept': 'application/json'})

            if login.status_code == requests.codes.ok:
                self.token = login.text;
                # Store the auth token
                # Create header for future request to the API
                self.authentication = {'X-Auth-Token': self.token, 'Content-Type': 'application/json'}
                self.header = self.authentication
                self.status_message = 'Login succeed!'
                return True
            else:
                self.status_message = 'Failed to login, status code: ' + login.status_code
                return False
        except OSError:
            print('Failed to login: ')

    def post_case(self, case):
        try:
            post = requests.post(self.base_url + '/inquiry/cableinquiry/involvedrecipients', headers=self.authentication
                                 , data=json.dumps(case))
            if post.status_code == 200:
                self.status_message = case + ' skapades'
                print(post.status_code, 'Case created')
            else:
                self.status_message = case + ' kunde inte skapas'
                print('Case was not created...', post.json())
        except IOError:
            print('Failed to post case: ')

    # Check what recipients who's affected by the case.
    def get_involved_recipients(self, cases):
        try:
            for case in cases:
                involved_recipients = requests.post(self.base_url + '/inquiry/cableinquiry/involvedrecipients',
                                                    headers=self.authentication,
                                                    data=json.dumps(case))
                if involved_recipients.status_code == requests.codes.ok:
                    print('Berörda LA: ', str(involved_recipients.json()))
                    print(str(json.dumps(involved_recipients.json(), default=lambda o: o.__dict__, sort_keys=True,
                                         indent=2)))
                else:
                    print('Failed to get involved recipients returned status code: ',
                          str(involved_recipients.status_code))
        except OSError:
            print('')
