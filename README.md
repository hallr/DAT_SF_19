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
12/14: [NumPy, Pandas, Viz, Model Evaluation](#class-5-numpy--pandas-visualization-model-evaluation) | 12/16: [Regression and Regularization](#class-6-regression-and-regularization) <br>**Project Question & Dataset Due**
12/21: **No Class** (Holiday Break) | 12/23: **No Class** (Holiday Break)
12/28: **No Class** (Holiday Break) | 12/30: **No Class** (Holiday Break)
1/4: [Logistic Regression](#class-7-logistic-regression) | 1/6: [Naive Bayes](#class-8-naive-bayes)
1/11: [Clustering](#class-9-clustering) | 1/13: [APIs & Web Scraping](#class-10-apis--web-scraping)
1/18: **No Class** (MLK Day) | 1/20: [Advanced Model Evaluation](#class-11-advanced-model-evaluation) <br>**Project First Draft Due**
1/25: [Decision Trees](#class-12-decision-trees) | 1/27: [Ensembles and Random Forests](#class-13-ensembles-and-random-forests)
2/1: [Support Vector Machines](#class-14-support-vector-machines) | 2/3: Dimensionality Reduction & PCA
2/8: Recommender Systems | 2/10: Text Processing / NLP <br>**Project Second Draft Due (Optional)**
2/15: **No Class** (President's Day) | 2/17: SQL & Databases
2/22: In-class Kaggle Competition or Advanced Topic | 2/24: Course Review & Where to Go from Here |
2/29: **Project Presentations & Project Due** | 3/2: **Project Presentations & Project Due**

_syllabus last updated: 02/01/2016_



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

### Class 6: Regression and Regularization

* Regression: Linear, Multiple, Polynomial ([slides](slides/06_regression.pdf))
* Regularization ([slides](slides/06_regression.pdf))

-----

### Class 7: Logistic Regression

* Logistic Regression ([slides](slides/07-logistic-regression.pdf))
* Lab: Logistic Regression ([notebook](labs/07-Logistic_Regression.ipynb))

**Resources:**
* To go deeper into logistic regression, read the first three sections of Chapter 4 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/).
* For a math-ier explanation of logistic regression, watch the first seven videos (71 minutes) from week 3 of Andrew Ng's [machine learning course](https://www.coursera.org/learn/machine-learning/home/info), or read the [related lecture notes](http://www.holehouse.org/mlclass/06_Logistic_Regression.html) compiled by a student.
* For more on interpreting logistic regression coefficients, read this excellent [guide](http://www.ats.ucla.edu/stat/mult_pkg/faq/general/odds_ratio.htm) by UCLA's IDRE and these [lecture notes](http://www.unm.edu/~schrader/biostat/bio2/Spr06/lec11.pdf) from the University of New Mexico.
* The scikit-learn documentation has a nice [explanation](http://scikit-learn.org/stable/modules/calibration.html) of what it means for a predicted probability to be calibrated.


-----

### Class 8: Naive Bayes

-----

### Class 9: Clustering

-----

### Class 10: APIs & Web Scraping

-----

### Class 11: Advanced Model Evaluation

* Model Evaluation, ROC, & AUC ([slides](slides/11-evaluation-ROC-AUC.pdf))
* Lab: Imbalanced Classes, Evaluation, & ROC (solutions) ([notebook](labs/11-Imbalance_and_Evaluation_ROC-Solutions.ipynb))

**ROC Resources:**
* Rahul Patwari has a great video on [ROC Curves](https://www.youtube.com/watch?v=21Igj5Pr6u4) (12 minutes).
* [An introduction to ROC analysis](http://people.inf.elte.hu/kiss/13dwhdm/roc.pdf) is a very readable paper on the topic.
* These [lesson notes](http://ebp.uga.edu/courses/Chapter%204%20-%20Diagnosis%20I/8%20-%20ROC%20curves.html) from a course at the University of Georgia include some simple, real-world examples of the use of ROC curves.
* ROC curves can be used across a wide variety of applications, such as [comparing different feature sets](http://research.microsoft.com/pubs/205472/aisec10-leontjeva.pdf) for detecting fraudulent Skype users, and [comparing different classifiers](http://www.cse.ust.hk/nevinZhangGroup/readings/yi/Bradley_PR97.pdf) on a number of popular datasets.
* This blog post about [Amazon Machine Learning](https://aws.amazon.com/blogs/aws/amazon-machine-learning-make-data-driven-decisions-at-scale/) contains a neat [graphic](https://media.amazonwebservices.com/blog/2015/ml_adjust_model_1.png) showing how classification threshold affects different evaluation metrics.

-----

### Class 12: Decision Trees

-----

### Class 13: Ensembles and Random Forests

-----

### Class 14: Support Vector Machines

* Support Vector Machines ([slides](slides/14-support-vector-machines.pdf))
* Lab: SVMs: Illuminating Advanced Classifiers ([notebook](labs/14-SVMs.ipynb))

**Additional Resources:**
* See the video embedded in the answer to [this question on Quora](https://www.quora.com/What-does-support-vector-machine-SVM-mean-in-laymans-terms) for a great animation of how kernels project non-linear classification problems into a higher dimensional space where they can be solved with a linear decision boundary / maximum margin hyperplane.
* For students who enjoy digging into the underlying mathematical concepts, [this reading](http://www.cs.colostate.edu/%7Easa/pdfs/howto.pdf) details the math behind support vector machines. Some of the examples in the lecture slides are taken from this reading.
* [Supervised learning superstitions cheat sheet](http://ryancompton.net/assets/ml_cheat_sheet/supervised_learning.html) is a very nice comparison of five classifiers we cover in the course (logistic regression, decision trees, KNN, Naive Bayes, and support vector machines).

-----




