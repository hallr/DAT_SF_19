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

#### Setup Info

**[Installation and Setup Checklist](other/setup_checklist.md)**

**[Git and Github Setup](other/git_github_setup.md)**

#### Project Info

**[Course Project Info](project/README.md)**

**[Course Project Examples](project/project-examples.md)**

### Course Schedule

Monday | Wednesday
--- | ---
11/30: Course Overview, [Introduction to Data Science](#class-1-introduction-to-data-science) | 12/2: [Version Control](#class-2-version-control)
12/7: [Intro to Python](#class-3-intro-to-python) | 12/9: [Intro to Machine Learning, KNN](#class-4-intro-to-machine-learning--classification-with-knn)
12/14: [NumPy, Pandas, Viz, Model Evaluation](#class-5-numpy--pandas-visualization-model-evaluation) | 12/16: Regression & Regularization <br>**Project Question & Dataset Due**
12/21: **No Class** (Holiday Break) | 12/23: **No Class** (Holiday Break)
12/28: **No Class** (Holiday Break) | 12/30: **No Class** (Holiday Break)
1/4: Logistic Regression | 1/6: Naive Bayes
1/11: Clustering | 1/13: APIs & Web Scraping
1/18: **No Class** (MLK Day) | 1/20: Advanced Model Evaluation <br>**Project First Draft Due**
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


**Git and Markdown Resources:**
* [Pro Git](http://git-scm.com/doc) is an excellent book for learning Git. Read [Chapter 1 - Getting Started](http://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) and [Chapter 2 - Git Basics](http://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) to gain a deeper understanding of version control and basic commands.
* Very quick [Git tutorial](https://try.github.io) by Github and Codeschool. Recommended practice!
* Github's [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) is a good starting point for learning github-flavored markdown.
* [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) provides a thorough set of Markdown examples with concise explanations.


**Command Line Resources:**
* If you want to go much deeper into the command line, [Data Science at the Command Line](http://shop.oreilly.com/product/0636920032823.do) is a great book. The [companion website](http://datascienceatthecommandline.com/) provides installation instructions for a "data science toolbox" (a virtual machine with many more command line tools), as well as a long reference guide to popular command line tools.

-----

### Class 3: Intro to Python

* Jupyter Notebook overview ([slides](slides/03-1_jupyter_notebook.pdf))
* Intro to Python ([slides](slides/03-2_python.pdf))
* Linear algebra refresher ([slides](slides/03-3_linear_algebra.pdf))

**Python Resources:**
* [Codecademy's Python course](http://www.codecademy.com/en/tracks/python): Good beginner material, including tons of in-browser exercises.
* [DataQuest](https://dataquest.io/): Similar interface to Codecademy, but focused on teaching Python in the context of data science.
* [Google's Python Class](https://developers.google.com/edu/python/): Slightly more advanced, including hours of useful lecture videos and downloadable exercises (with solutions).
* [A Crash Course in Python for Scientists](http://nbviewer.ipython.org/gist/rpmuller/5920182): Read through the Overview section for a quick introduction to Python.
* [Python for Informatics](http://www.pythonlearn.com/book.php): A very beginner-oriented book, with associated [slides](https://drive.google.com/folderview?id=0B7X1ycQalUnyal9yeUx3VW81VDg&usp=sharing) and [videos](https://www.youtube.com/playlist?list=PLlRFEj9H3Oj4JXIwMwN1_ss1Tk8wZShEJ).


-----

### Class 4: Intro to Machine Learning & Classification with KNN

* Intro to Machine Learning ([slides](slides/04_intro_ml_knn.pdf))
* Lab: KNN classification with Scikit-learn ([notebook](labs/05_knn_sklearn.ipynb))

**ML Resources**:
* For a more formal, in-depth introduction to machine learning, read section 2.1 (14 pages) of Hastie and Tibshirani's excellent book, [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/). (It's a free PDF download!)

**KNN Resources:**
* [A Detailed Introduction to KNN](https://saravananthirumuruganathan.wordpress.com/2010/05/17/a-detailed-introduction-to-k-nearest-neighbor-knn-algorithm/) is a bit dense, but provides a more thorough introduction to KNN and its applications.
* Browse through the scikit-learn documentation for KNN to get a sense of how it's organized: [user guide](http://scikit-learn.org/stable/modules/neighbors.html), [module reference](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.neighbors), [class documentation](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)


-----

### Class 5: numpy & pandas, Visualization, Model Evaluation

* Lab: numpy ([notebook](labs/05_numpy_pandas_bokeh.ipynb))
* Lab: pandas ([notebook](labs/05_numpy_pandas_bokeh.ipynb))
* Lab: Visualization with Bokeh ([notebook](labs/05_numpy_pandas_bokeh.ipynb))
* Model Evaluation, incl. Cross Validation ([slides](slides/05_model_evaluation.pdf))
* Lab: Cross validation with Python and Scikit-learn ([notebook](labs/05_model_evaluation_lab.ipynb))

**Pandas Resources:**
* To learn more Pandas, review this [three-part tutorial](http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/).
* Browsing or searching the Pandas [API Reference](http://pandas.pydata.org/pandas-docs/stable/api.html) is an excellent way to locate a function even if you don't know its exact name.
* If you want to go really deep into Pandas (and NumPy), read the book [Python for Data Analysis](http://shop.oreilly.com/product/0636920023784.do) by Wes McKinney, the creator of Pandas. Ping me on Slack for a discount code.
* Here are examples of different types of [joins in Pandas](http://www.gregreda.com/2013/10/26/working-with-pandas-dataframes/#joining), for when you need to figure out how to merge two DataFrames.
* **Optional:** Read the [Teaching Assistant Evaluation dataset](https://archive.ics.uci.edu/ml/datasets/Teaching+Assistant+Evaluation) into Pandas, create the X and y objects (the response variable is "class attribute"), and go through scikit-learn's 4-step modeling process. (There's no need to submit your code unless you have a question or would like feedback!)

**Model Evaluation Resources**
* For another explanation of training error versus testing error, the bias-variance tradeoff, and train/test split (also known as the "validation set approach"), watch Hastie and Tibshirani's video on [estimating prediction error](https://www.youtube.com/watch?v=_2ij6eaaSl0&t=2m34s) (12 minutes, starting at 2:34).
* Caltech's Learning From Data course includes a fantastic video on [visualizing bias and variance](http://work.caltech.edu/library/081.html) (15 minutes).
* [Random Test/Train Split is Not Always Enough](http://www.win-vector.com/blog/2015/01/random-testtrain-split-is-not-always-enough/) explains why random train/test split may not be a suitable model evaluation procedure if your data has a significant time element.

**Additional Resources:**
* [What I do when I get a new data set as told through tweets](http://simplystatistics.org/2014/06/13/what-i-do-when-i-get-a-new-data-set-as-told-through-tweets/) is a fun (yet enlightening) look at the process of exploratory data analysis.

-----

### Class 6: Regression & Regularization

* Regression: Linear, Multiple, Polynomial ([slides](slides/06_regression.pdf))
* Regularization ([slides](slides/06_regression.pdf))

-----

### Resources for Continued Learning over the Holiday Break




