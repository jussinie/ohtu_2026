*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  arto
    Set Password  salainen1
    Set Password Confirmation  salainen1
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ar
    Set Password  salainen1
    Set Password Confirmation  salainen1
    Submit Credentials
    Register Should Fail With Message  Username must be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  arto
    Set Password  sala1
    Set Password Confirmation  sala1
    Submit Credentials
    Register Should Fail With Message  Password must be at least 8 characters

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  salainen1
    Set Password Confirmation  salainen1
    Submit Credentials
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Submit Credentials
    Click  button >> text=Register

Register Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

