*** Settings ***
Documentation     Starter functional tests for the local Online Movie Booking System.
...               Inspect the actual HTML and adjust locators before relying on results.
Library           SeleniumLibrary
Suite Setup       Open Application
Suite Teardown    Close All Browsers
Test Setup        Go To    ${BASE_URL}

*** Variables ***
${BASE_URL}       http://127.0.0.1:8000
${BROWSER}        chrome
${SEARCH_INPUT}   name=q
${SEARCH_BUTTON}  css:button[type="submit"]

*** Test Cases ***
FT01 Home Page Loads
    [Documentation]    Basic smoke check that the local application responds.
    Title Should Not Be Empty

FT02 Search Existing Movie
    [Documentation]    Searches for Venom; adjust selectors to match the app.
    Wait Until Element Is Visible    ${SEARCH_INPUT}    10s
    Input Text    ${SEARCH_INPUT}    Venom
    Click Button    ${SEARCH_BUTTON}
    Wait Until Page Contains    Venom    10s

FT03 Search Missing Movie
    [Documentation]    Checks the no-results flow; expected text may need adjustment.
    Wait Until Element Is Visible    ${SEARCH_INPUT}    10s
    Input Text    ${SEARCH_INPUT}    Nonexistent123XYZ
    Click Button    ${SEARCH_BUTTON}
    Wait Until Page Contains    No    10s

*** Keywords ***
Open Application
    Open Browser    ${BASE_URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    2s
