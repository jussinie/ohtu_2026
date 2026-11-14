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

Register With Matching Password Confirmation
    Set Username  arto
    Set Password  salainen1
    Set Password Confirmation  salainen1
    Submit Credentials
    Register Should Succeed

Register With Nonmatching Password Confirmation
    Set Username  arto
    Set Password  salainen1
    Set Password Confirmation  salainen2
    Submit Credentials
    Register Should Fail With Error Message

Register With Password Containing Numbers
    Set Username  arto
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Password Containing Special Character
    Set Username  arto
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Submit Credentials
    Register Should Succeed

Register With Password Made Of Lowercase Letters
    Set Username  arto
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Submit Credentials
    Register Should Fail With Error Message

Register With Password Made Of Mixed Case Letters
    Set Username  arto
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Submit Credentials
    Register Should Fail With Error Message

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

Register Should Fail With Error Message
    Register Page Should Be Open
    ${message}=  Get Text  li
    Should Not Be Empty  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
