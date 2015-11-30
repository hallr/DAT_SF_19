## Setup checklist

This is a checklist to confirm that your laptop is set up properly for DAT19. If at any point you get an error message, please note the error message and we will help you to fix it! If you don't get any error messages, you are properly set up.

Please post a message in the "setupchecklist" channel in Slack once you have walked through the entire checklist. That way, we will know whether or not we need to follow up with you.

### Installation and Setup

### Installation and Setup
* Install the [Anaconda distribution](http://continuum.io/downloads) of Python 2.7x.
* Install [Git](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and create a [GitHub](https://github.com/) account.
* Once you receive an email invitation from [Slack](https://slack.com/), join our team and add your photo!

### GitHub
* Log into your GitHub account, and "star" the DAT19 repository (the one you are looking at right now) by clicking the Star button in the upper right corner of the screen.

### Git
* Open a command line application:
    * For Windows, we recommend [Git Bash](http://git-scm.com/download/win) instead of Git Shell (which uses Powershell).
    * For Mac, you will probably be using Terminal, or another command line tool of your choice.
* Type `git config --global user.name "YourFirstName YourLastName"` (including the quotes)
* Type `git config --global user.email "youremail@domain.com"` (use the email address associated with your GitHub account)
* Type `git clone https://github.com/hallr/DAT_SF_19.git`
    * This will create a folder called "DAT_SF_19" in the working directory of your local computer, and will copy the repository into that folder. (If you don't know what the working directory is, type `pwd`.)
    * You are welcome to move the DAT19 folder to another location on your computer, or delete it entirely. We will explain the purpose of cloning this repository during the course.

### Python
* While still at the command line:
    * Type `conda list` (if you choose not to use Anaconda, this will generate an error)
    * Type `python` to open the Python interpreter
* While in the Python interpreter:
    * Look at the Python version number. It should start with 2.7.
    * Type `import pandas`
    * Type `exit()` to exit the interpreter. You can now close the command line application.

