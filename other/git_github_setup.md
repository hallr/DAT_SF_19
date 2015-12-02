## Git Configuration and Github Setup

**IMPORTANT: We will step through this together in class. You do not need to do this on your own.**

### GitHub
* Log into your GitHub account, and "star" the DAT\_SF\_19 repository (the one you are looking at right now) by clicking the Star button in the upper right corner of the screen.

### Git
* Make sure you have [Sublime Text 2](http://www.sublimetext.com/2) installed.
* Open a command line application:
    * For Windows, we recommend [Git Bash](http://git-scm.com/download/win) instead of Git Shell (which uses Powershell).
    * For Mac, you will probably be using Terminal, or another command line tool of your choice.

1. Configure your global git settings
  1. First, cd to your DAT\_SF\_19 directory on your laptop
  2. Type `git config --list` to see your current git configuration settings. What is the `user.name` setting? What is the `user.email` setting? Next, we will configure git to use your github user name and email address.
  3. Type `git config --global user.name "YourFirstName YourLastName"` (including the quotes)
  4. Type `git config --global user.email "youremail@domain.com"` (use the email address associated with your GitHub account)
  5. Type `git config --list` again. Those setting should be updated to match the config changes you just made.


<!--Install `subl` command.
* In this step, we will install a new command line command that will enable you to launch Sublime Text 2 from the command line. We will also set Sublime Text 2 as the default editor for git. The default text editor for git is emacs, so unless you are comfortable working in emacs, we strongly recommend that you set up git to use Sublime Text 2.
-->


* Type `git config --global user.name "YourFirstName YourLastName"` (including the quotes)
* Type `git config --global user.email "youremail@domain.com"` (use the email address associated with your GitHub account)
* Type `git clone https://github.com/hallr/DAT_SF_19.git`
    * This will create a folder called "DAT_SF_19" in the working directory of your local computer, and will copy the repository into that folder. (If you don't know what the working directory is, type `pwd`.)
    * You are welcome to move the DAT19 folder to another location on your computer, or delete it entirely. We will explain the purpose of cloning this repository during the course.