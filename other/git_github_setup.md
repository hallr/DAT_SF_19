## Git Configuration and Github Setup

**IMPORTANT: We will step through this together in class. You do not need to do this on your own.**

### GitHub
* Log into your GitHub account, and "star" the DAT\_SF\_19 repository (the one you are looking at right now) by clicking the Star button in the upper right corner of the screen.

### Git
* Make sure you have [Sublime Text 2](http://www.sublimetext.com/2) installed.
* Open a command line application:
    * For Windows, we recommend [Git Bash](http://git-scm.com/download/win) instead of Git Shell (which uses Powershell).
    * For Mac, you will probably be using Terminal, or another command line tool of your choice.

1. Configure your global git user name and email settings:

  1. Type `git config --list` to see your current git configuration settings. What is the `user.name` setting? What is the `user.email` setting? Next, we will configure git to use your github user name and email address.
  2. Type `git config --global user.name "YourFirstName YourLastName"` (including the quotes)
  3. Type `git config --global user.email "youremail@domain.com"` (use the email address associated with your GitHub account)
  4. Type `git config --list` again. Those setting should be updated to match the config changes you just made.

2. Clone the course repo to your laptop:
  1. cd to the place where you want to copy the course repo. Your desktop is a great place for this while in the course, but any place where you can easily find it via the command line is fine. The following will create a folder called "DAT_SF_19" in the working directory of your local computer, and will copy the repository into that folder. (If you don't know what the working directory is, type `pwd`.)
  2. Clone the course repo to your laptop by typing `git clone https://github.com/hallr/DAT_SF_19.git`
  3. cd into the DAT_SF_19 directory that is now on your laptop. List the contents of that directory. What do you see?
  4. **NOTE**: We will not be working in the course repo. We will use this directory to pull new class content from github. We will then copy any files to our personal homework directory to do work. This avoids potential conflicts with the course repo!

3. Install the `subl` command: In this step, we will install a new command that will enable us to launch Sublime Text 2 from the command line. We will also set Sublime Text 2 as the default editor for git. The default text editor for git is the system default. So, unless you are comfortable working in vi (on OS X), we strongly recommend that you set up git to use Sublime Text 2.
  1. **STOP. We will do this together!** Copy/paste the following to your command line. This creates a symlink. Make sure it copies exactly and that you have not missed any characters!

  ```sudo ln -s "/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl" /usr/local/bin/subl```

  2. Enter the password for your computer when prompted.
  3. Type `subl README.md`. Sublime should launch a new window with the markdown for the course schedule (remember you should be in the course repo). If this displays as expected, simply close Sublime Text.

4. Make Sublime Text 2 your default text editor for git:
  1. Type `git config --global core.editor "subl -n -w"`
  2. To test this config setting, type `git config -e` to launch the default text editor for git. Again, Sublime Text should display. Close Sublime Text.

5. Next, we will set up your personal homework directory:
  1. Leave the command line for a moment and return to your browser. You should already be logged in to your github account.
  2. Go to your profile. Click on the "Repositories" tab.
  3. Click on the "New" button.
  4. Name your new repo `DAT_SF_19_work`.
  5. Give it a description, such as "YourName's work repo for the DAT19 course at General Assembly San Francisco".
  6. Click the checkbox to "Initialize this repository with a README". You need at least one file in the repo to be able to clone it.
  7. You should see your new repo on Github.
  8. Copy the HTTPS URL to clone the repo.
  9. Return to the Terminal / your command line.
  10. **IMPORTANT** Cd out of the DAT_SF_19 course repo! DO NOT clone your homework repo inside the class repo!
  11. cd to where you want to have your work repo.
  12. Type `git clone` and paste the URL to your new personal work repo. Git will clone your new personal work repo from Github to your laptop.

6. Finally, let's get some practice with our new workflow!

