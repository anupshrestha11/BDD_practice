from behave import given, when, then, step
import requests
from behave.model import Scenario

api_endpoints = {}
request_headers = {}
response_codes = {}
response_texts = {}
request_bodies = {}
api_url = ""


@given(u'I set sample REST API url')
def step_impl(context):
    global api_url
    api_url = "http://jsonplaceholder.typicode.com"


# START POST Scenario
@given(u'I set POST posts api endpoint')
def step_impl(context):
    api_endpoints['POST_URL'] = api_url + '/posts'
    print('url :' + api_endpoints['POST_URL'])


@when(u'I set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    request_headers['Content-Type'] = header_content_type


# You may also include "And" or "But" as a step
# - these are renamed by behave to take the name of their preceding step, so:
@when('Set request Body')
def step_impl(context):
    request_bodies['POST'] = {"title": "foo", "body": "bar", "userId": "1"}


@when('Send a POST HTTP request')
def step_impl(context):
    response = requests.post(url=api_endpoints['POST_URL'], json=request_bodies['POST'], headers=request_headers)
    response_texts['POST'] = response.text
    statuscode = response.status_code
    response_codes['POST'] = statuscode


@then('I receive valid HTTP response code 201')
def step_impl(context):
    print('Post rep code :' + str(response_codes['POST']))
    assert response_codes['POST'] is 201


@then(u'Response BODY "{request_name}" is non-empty.')
def step_impl(context, request_name):
    print('request_name: ' + request_name)
    print(response_texts)
    assert response_texts[request_name] is not None


# End Scenario

# Start of Scenario 2
@given('I set GET posts api endpoint')
def step_impl(context):
    api_endpoints['GET_URL'] = api_url + '/posts'
    print('url :' + api_endpoints['GET_URL'])


@when("Send a GET HTTP request")
def step_impl(context):
    response = requests.get(url=api_endpoints['GET_URL'], headers=request_headers)
    response_texts['GET'] = response.text
    statuscode = response.status_code
    response_codes['GET'] = statuscode


@then("I receive valid HTTP response code 200")
def step_impl(context):
    print('Post rep code :' + str(response_codes['GET']))
    assert response_codes['GET'] is 200


# End Scenario 2

# Start of Scenario 3
@given('I set PUT posts api endpoint for "{id}"')
def step_impl(context, id):
    api_endpoints["PUT_URL"] = api_url + "/posts/" + id
    print('url :' + api_endpoints['PUT_URL'])


@when('I set Update request Body')
def step_impl(context):
    request_bodies['PUT'] = {"title": "foo", "body": "bar", "userId": "1", "id": "1"}


@when('Send PUT HTTP request')
def step_impl(context):
    response = requests.put(url=api_endpoints['PUT_URL'], json=request_bodies['PUT'], headers=request_headers)
    response_texts['PUT'] = response.text
    statuscode = response.status_code
    response_codes['PUT'] = statuscode


@then('I receive valid HTTP response code 200 for "PUT"')
def step_impl(context):
    print('Post rep code :' + str(response_codes['PUT']))
    assert response_codes['PUT'] is 200


# End Scenario 3

# Start of Scenario 4
@given('I set DELETE posts api endpoint for "{id}"')
def step_impl(context, id):
    api_endpoints['DELETE_URL'] = api_url + "/posts/" + id
    print('url :' + api_endpoints['DELETE_URL'])


@when('Send DELETE HTTP request')
def step_impl(context):
    response = requests.delete(url=api_endpoints['DELETE_URL'], headers=request_headers)
    response_texts['DELETE'] = response.text
    statuscode = response.status_code
    response_codes['DELETE'] = statuscode


@then('I receive valid HTTP response code 200 for "DELETE"')
def step_impl(context):
    print('Post rep code :' + str(response_codes['DELETE']))
    assert response_codes['DELETE'] is 200
