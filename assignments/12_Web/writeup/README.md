# Crypto II Writeup

Name: Holland Emery
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: 0201

## Assignment Writeup

### Part 1 (40 Pts)

### Part 2 (60 Pts)

level 1) all I had to do was type <script>alert();</script> into the text field to get an alert
level 2) for level 2 In typed <img src = "asdfg" onerror = alert()> this tried to display the image at the url "asdfg" and when the image could not be displayed it ran alert()
level 3) for level 3 I added '><img src = a onerror = alert()> which caused the website to try and display an image which alerted when it failed similar to level 2
level 4) for level 4 i set the time to 3'); alert(' which caused the website to run the command to start the timer with time 3 then run the alert command startTimer('   3'); alert('   );
level 5) for level 5 i changed the frame url after clicking the signup link to be xss-game.../frame/signup?next=javascript:alert() so that when the next link was clicked it ran alert instead of redirecting to confirm
level 6) for level 6 i changed the frame url to level6/frame#//www.google.com/jsapi?callback=alert which caused the website to run the javascript for google.com/jsapi?callback=alert which runs the alert command it also avoided the check for urls begining with https since it does not begin with https
