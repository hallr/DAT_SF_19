## DAT SF 19 Course Repository

Course materials for [General Assembly's Data Science course](https://generalassemb.ly/education/data-science/san-francisco) in San Francisco (11/30/15 - 3/2/16).

**Instructor:** [Rob Hall](https://generalassemb.ly/instructors/rob-hall/1864)

**TA's:** 
* Justin Breucop
* Dave Yerrington

#### Office Hours

Who | When
--- | ---
Justin | Sundays 3-6pm at GA
Dave | Fridays 6-8pm at GA
Rob | Slack and by appointment

#### Slack

Once you've received the invitation to Slack, please log in and **add your picture**!
Slack will be the primary way we communicate with each other.

**[Installation and Setup Checklist](other/setup_checklist.md)**

**[Git and Github Setup](other/git_github_setup.md)**

**[Course Project Info](project/README.md)**

**[Course Project Examples](project/project-examples.md)**

### Course Schedule

Monday | Wednesday
--- | ---
11/30: Course Overview, [Introduction to Data Science](#class-1-introduction-to-data-science) | 12/2: [Version Control](#class-2-version-control)
12/7: Intro to Python | 12/9: Intro to Machine Learning, KNN
12/14: Pandas, Viz, Model Evaluation | 12/16: Regression & Regularization <br>**Project Question & Dataset Due**
12/21: **No Class** (Holiday Break) | 12/23: **No Class** (Holiday Break)
12/28: **No Class** (Holiday Break) | 12/30: **No Class** (Holiday Break)
1/4: Logistic Regression | 1/6: APIs & Web Scraping
1/11: Naive Bayes | 1/13: Advanced Model Evaluation
1/18: **No Class** (MLK Day) | 1/20: Clustering <br>**Project First Draft Due**
1/25: Decision Trees | 1/27: Ensembling Techniques
2/1: Dimensionality Reduction | 2/3: Support Vector Machines
2/8: Recommender Systems | 2/10: SQL, Databases <br>**Project Second Draft Due (Optional)**
2/15: **No Class** (President's Day) | 2/17: Advanced Topic or Guest Speaker
2/22: Advanced Topic or Guest Speaker | 2/24: Course Review |
2/29: **Project Presentations & Project Due** | 3/2: **Project Presentations & Project Due**

_syllabus last updated: 12/12/2015_



-----

### Class 1: Introduction to Data Science
* Welcome from General Assembly staff
* Course overview ([slides](slides/01_course_intro.pdf))
* Introduction to data science ([slides](slides/01_intro_to_data_science.pdf))
* Command line & exercise ([code](code/02_command_line.md))
* Exit tickets


**Homework:**
* Work through GA's friendly [command line tutorial](http://generalassembly.github.io/prework/command-line/#/) using Terminal (Linux/Mac) or Git Bash (Windows), and then browse through this [command line reference](code/02_command_line.md).
* Watch videos 1 through 8 (21 minutes) of [Introduction to Git and GitHub](https://www.youtube.com/playlist?list=PL5-da3qGB5IBLMp7LtN8Nc3Efd4hJq0kD).
* If your laptop has any setup issues, please work with us to resolve them by Wednesday.

**Resources:**
* For a useful look at the different types of data scientists, read [Analyzing the Analyzers](http://cdn.oreillystatic.com/oreilly/radarreport/0636920029014/Analyzing_the_Analyzers.pdf) (32 pages).
* For some thoughts on what it's like to be a data scientist, read these short posts from [Win-Vector](http://www.win-vector.com/blog/2012/09/on-being-a-data-scientist/) and [Datascope Analytics](http://datascopeanalytics.com/what-we-think/2014/07/31/six-qualities-of-a-great-data-scientist).
* Quora has a [data science topic FAQ](https://www.quora.com/Data-Science) with lots of interesting Q&A.

-----

### Class 2: Version Control
* Final project presentations from other class
* Q&A on [course project](project/README.md) expectations & schedule
  * [public data sources](project/public_data.md)
* Version Control with Git and GitHub ([slides](slides/02_version_control_git.pdf))
* [Git Configuration and Github setup](other/git_github_setup.md)
* Moved to Class 3: Intro to Python ([slides](slides/02_intro_to_python.pdf))
* Exit tickets


**Homework:**
* If you haven't already, complete the homework exercise listed in the [command line introduction](code/02_command_line.md#homework-exercise). Create a Markdown document that includes your answers and the code you used to arrive at those answers. Add this file to a GitHub repo that you'll use for all of your coursework, and submit a link to your repo using the homework submission form.

<!--
* Review the code from the [beginner](code/00_python_beginner_workshop.py) and [intermediate](code/00_python_intermediate_workshop.py) Python workshops. If you don't feel comfortable with any of the content (up through the "dictionaries" section), you should spend some time this weekend practicing Python. Here are my recommended resources:
    * If you like learning from a book, [Python for Informatics](http://www.pythonlearn.com/html-270/) has useful chapters on strings, lists, and dictionaries.
    * If you prefer interactive exercises, try these lessons from [Codecademy](http://www.codecademy.com/en/tracks/python): "Python Lists and Dictionaries" and "A Day at the Supermarket".
    * If you have more time, try these much longer lessons from [DataQuest](https://dataquest.io/missions): "Find the US city with the lowest crime rate" and "Discover weather patterns in LA".
    * If you've already mastered these topics and want more of a challenge, try solving the second [Python Challenge](http://www.pythonchallenge.com/) and send me your code in Slack.
* If there are specific Python topics you want me to cover next week, send me a Slack message.
-->

**Git and Markdown Resources:**
* [Pro Git](http://git-scm.com/doc) is an excellent book for learning Git. Read [Chapter 1 - Getting Started](http://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) and [Chapter 2 - Git Basics](http://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) to gain a deeper understanding of version control and basic commands.
* Very quick [Git tutorial](https://try.github.io) by Github and Codeschool. Recommended practice!
* Github's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) is a good starting point for learning github-flavored markdown.
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) provides a thorough set of Markdown examples with concise explanations.

<!--
* If you want to practice a lot of Git (and learn many more commands), [Git Immersion](http://gitimmersion.com/) looks promising.
* If you want to understand how to contribute on GitHub, you first have to understand [forks and pull requests](http://www.dataschool.io/simple-guide-to-forks-in-github-and-git/).
* [GitRef](http://gitref.org/) is a great reference guide for Git commands, and [Git quick reference for beginners](http://www.dataschool.io/git-quick-reference-for-beginners/) is a shorter guide with commands grouped by workflow.
-->

**Command Line Resources:**
* If you want to go much deeper into the command line, [Data Science at the Command Line](http://shop.oreilly.com/product/0636920032823.do) is a great book. The [companion website](http://datascienceatthecommandline.com/) provides installation instructions for a "data science toolbox" (a virtual machine with many more command line tools), as well as a long reference guide to popular command line tools.


-----

<!--
### Homework Schedule

Please submit completed homework assignments by pushing them to your homework repo under your own userid and then telling us where to find your homework via the [homework submission form](http://goo.gl/forms/QBZBG4P3bm).

HW | Topics | Dataset | Assigned | Due
--- | --- | --- | --- | ---
1 | Data Exploration | titanic | 3/11 | 3/16
2 | KNN & Cross Validation | iris | 3/18 | 3/25
FP1 | Elevator Pitch | N/A | 3/23 | 4/1
3 | Decision Trees | bank | 3/30 (as mandatory) | 4/8 (extended)
4 | Logistic Regression, ROC/AUC, & Imbalanced Classes | spam | 4/13 | 4/20
FP2 | [First Draft](https://github.com/ga-students/DAT_SF_13/blob/master/project/dat_project.md#april-26-first-draft-due) of Final Project | yours | 4/13 | 4/27
FP3 | [Peer Feedback](https://github.com/ga-students/DAT_SF_13/blob/master/project/peer_review_guidelines.md) on FP First Draft | yours | 4/27 | 5/4

### Communication

#### Office Hours

instructor | times available | method
:----------|:-------------------|:--
Ankit      | Wednesday, 6:00 - 6:30 PM | in person before class, slack, hangouts by appointment
Chetan	   | Monday, 6:00 - 6:30 PM | in person before class, hangouts by appointment
Matt       | Thursday, 6:00 - 7:00 PM | in person (at GA in "the concourse"), slack, hangouts by appointment
Rob        | Tues & Thurs, all day   | slack (quickest response) or hangouts by appointment

Please use email or Slack to schedule office hours. Use [office hours] in the subject line as it can help us find the emails easier and reply more quickly.
-->
