from django.http import HttpResponse
from django.shortcuts import render, redirect
from oauth2_client.credentials_manager import ServiceInformation, CredentialManager

FORM_SUBMIT_URL   = 'http://authorization-ptl-df6521cb-867e48b1.libcurl.so/oauth/authorize'
TOKEN_SERVICE_URL = 'http://authorization-ptl-df6521cb-867e48b1.libcurl.so/oauth/token'
CLIENT_ID='68043aa9d1b022283f53a94da7bc9bac3577449a53aaab8a26d09bb73df9a991'
CLIENT_SECRET='b7fc93cdcf489b05b7a64b00307d6808da6fb2dc828f97e92e365e380b6c6c55'
REDIRECT_URI = "http://oxee.herokuapp.com/oauth/get_token/"
SCOPES = ['email']


def csrf_form_html(request):
    return render(request, "csrf_form.html", {
        'FORM_SUBMIT_URL': FORM_SUBMIT_URL,
        'REDIRECT_URI': REDIRECT_URI,
        'CLIENT_ID': CLIENT_ID,
    })

def client(request):

    service_information = ServiceInformation(authorize_service=FORM_SUBMIT_URL,
                                             token_service=TOKEN_SERVICE_URL,
                                             client_id=CLIENT_ID,
                                             client_secret=CLIENT_SECRET,
                                             scopes=SCOPES)

    # manager = CredentialManager(service_information,
    #                             proxies=dict(http='http://localhost:3128', https='http://localhost:3128'))

    manager = CredentialManager(service_information)

    url = manager.generate_authorize_url(REDIRECT_URI, 'state_test')
    print('Open this url in your browser\n%s', url)

    return redirect(url)


def get_token(request):

    service_information = ServiceInformation(authorize_service=FORM_SUBMIT_URL,
                                             token_service=TOKEN_SERVICE_URL,
                                             client_id=CLIENT_ID,
                                             client_secret=CLIENT_SECRET,
                                             scopes=SCOPES)

    manager = CredentialManager(service_information)

    code = request.GET.get('code')
    print('Code got = %s', code)
    # manager.init_with_authorize_code(REDIRECT_URI, code)
    manager._token_request(manager._grant_code_request(code, REDIRECT_URI), False)
    print("Code:", code, 'Token:', manager._access_token)
    return HttpResponse(manager._access_token)


def autosubmit_forms(request):
    return render(request, "autosubmit_forms.html")

def autosubmit_iframe(request):
    return render(request, "autosubmit_iframe.html")

