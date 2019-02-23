# Writeup 2 - OSINT

Name: *Holland Emery*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Holland Emery

## Assignment Writeup

### Part 1 (45 pts)

V0idcache's real name is Elizabeth Moffet, She works at Elite Banking and the website URL for Elite Banking  is 1337bank.money.
Elizabeth Moffet has a twitter and lives in the Netherlands.  The IP address for the website is 142.93.136.81 and the server 
is located in Canada, I found this information through dnsdumpster.com.  I found three flags related to the website the first
flag was in the source code of the website, CMSC389R-{h1dd3n_1n_plain_5ight}, I found the second flag by going the the robots.txt
webpage and seeing that there was a secret_directory page and on the page was the second flag, CMSC389R-{h1ding_fil3s_in_r0bots_L0L}.
The third flag related to the website was found on dnsdumpster.com and is CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5}. The open ports on the 
website are 22, 25, 80, and 1337, I found these by running nmap on the IP address of the website. port 22 is for SSH, 25 is for
smtp, 80 for http, and finaly 1337 for the login. The server is running Ubuntu 18.04 
### Part 2 (75 pts)

The bruteforce code that I wrote to gain access to the server found that the password is linkinpark. Once I had the password
I logged into the server and found two more flags, they were both in the home directory.  The first flag was in a file called
flag.txt and is CMSC389R-{brut3_f0rce_m4ster}.  The second flag is in home/files in a file named AB4300.txt and is 
CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}. I knew to look in this specific file because of a pastebin log that i found between
v0idcache and fl1nch which mentioned a file called AB4300.txt.