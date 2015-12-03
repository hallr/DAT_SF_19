## Git Configuration and Github Setup

**IMPORTANT: We will step through this together in class. You do not need to do this on your own.**

### GitHub
* Log into your GitHub account, and "star" the DAT\_SF\_19 repository (the one you are looking at right now) by clicking the Star button in the upper right corner of the screen.

### Git
* You should already have git installed.
* Make sure you have [Sublime Text 2](http://www.sublimetext.com/2) installed.
* Open a command line application:
    * For Windows, we recommend [Git Bash](http://git-scm.com/download/win) instead of Git Shell (which uses Powershell).
    * For Mac, you will probably be using Terminal, or another command line tool of your choice.

1. Configure your global git user name and email settings:

  1. Type `git config --list` to see your current git configuration settings. What is the `user.name` setting? What is the `user.email` setting? Next, we will configure git to use your github user name and email address.
  2. Type `git config --global user.name "YourFirstName YourLastName"` (including the quotes)
  3. Type `git config --global user.email "youremail@domain.com"` (use the email address associated with your GitHub account)
  4. Type `git config --list` again. Those setting should be updated to match the config changes you just made. Note that you can also check an specific setting by typing `git config --global` with no argument.

2. Fork the course repo to your Github user account:
  1. In your browser, go to the course repo at `https://github.com/hallr/DAT_SF_19`
  2. Click on the "Fork" button on that page.
  3. After a few seconds, you should see a fork of the repo under YOUR github account.

3. Clone YOUR FORK of the course repo to your laptop:
  1. cd to the place where you want to copy the course repo. Your desktop is a great place for this while in the course, but any place where you can easily find it via the command line is fine. Create a "General Assembly" directory.
  2. cd into the General Assembly directory. The following will create a folder called "DAT_SF_19" in that directory of your computer, and will copy the repository into that folder.
  3. Clone the course repo to your laptop by typing `git clone` and the HTTPS URL for your forked repo. It will be of the form `https://github.com/<yourGithubUsername>/DAT_SF_19.git`
  4. cd into the DAT_SF_19 directory that is now on your laptop. List the contents of that directory. What do you see?
  5. **IMPORTANT**: Always copy and rename files before modifying them in your fork of the course repo. If you modify a course file, then git will detect a merge conflict the next time you pull from the updated course repo. These are no fun.
  6. Create a folder called "Homework" in your repo. This is the folder in which you will do your work and submit homework assignments.

4. Setup [remotes](http://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes):
  1. Set up your fork to pull the latest content from the instructor repo in Rob's github account. To do this, we'll create what's called an upstream remote. Type `git remote add instructor https://github.com/hallr/DAT_SF_19.git`
  2. Type `git remote -v` to confirm your remotes are set up correctly.
  3. From now on, to get the latest content from the course repo, type `git pull instructor`


5. **OS X / Unix ONLY** Install the `subl` command: In this step, we will install a new command that will enable us to launch Sublime Text 2 from the command line. We will also set Sublime Text 2 as the default editor for git. The default text editor for git is the system default. So, unless you are comfortable working in vi (on OS X), we strongly recommend that you set up git to use Sublime Text 2.
  1. **STOP. We will do this together!** Copy/paste the following to your command line. This creates a symlink. Make sure it copies exactly and that you have not missed any characters!

  ```sudo ln -s "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl```

  2. Enter the password for your computer when prompted.
  3. Type `subl README.md`. Sublime should launch a new window with the markdown for the course schedule (remember you should be in the course repo). If this displays as expected, simply close Sublime Text.

6. **OS X / Unix ONLY** Make Sublime Text 2 your default text editor for git:
  1. Type `git config --global core.editor "subl -n -w"`
  2. To test this config setting, type `git config -e` to launch the default text editor for git. Again, Sublime Text should display. Close Sublime Text.

7. Finally, let's get some practice with our new workflow!
  1. Create a new text file in your Homework folder. Call it `temp.txt` or something similar. It can be an empty text file.
  2. Type `git status`. What do you see?
  3. Type 'git add` and your file name.
  4. Type `git status` again. What changed?
  5. Type `git commit -m "initial commit"`. Hit enter.
  6. Switch back to your browser to view your work repo on Github and refresh the page. Do you see any files other than the README.md?
  7. Switch back to the command line and type `git push -u origin master`. What happens?
  8. Switch back to Github and refresh the page for your repo. What do you see now?

8. **Bonus question**: What do you think will happen if you type `git push -u instructor master`? Why?


