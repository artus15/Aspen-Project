*** Settings ***
Library  RequestsLibrary

*** Variables ***
${URL}  http://127.0.0.1:8000/

*** Test Cases ***
Create new player
    [Documentation]   Creating a new player
    Create Session   Create_new_player   ${URL}
    ${data}   Create Dictionary   name=tester   password=psswrd   wins=0
    ${response}=   RequestsLibrary.POST On Session   Create_new_player   createPlayer/   json=${data}

Update player info
    [Documentation]   Update some user info
    Create Session   Update_player   ${URL}
    ${data}   Create Dictionary   name=tester2   password=psswrd2   wins=0
    ${response}=   RequestsLibrary.PATCH On Session   Update_player   updatePlayer/9/   json=${data}
    Log to console   Player updated info: ${response.json()}
    Should Be Equal As Strings   ${response.json()}[name]   tester2
    Should Be Equal As Strings   ${response.json()}[password]   psswrd2

Delete existing player
    [Documentation]   Delete existing player
    Create Session   Delete_player   ${URL}
    ${response}=   delete on session   Delete_player   deletePlayer/9/