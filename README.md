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
2/1: [Support Vector Machines](#class-14-support-vector-machines) | 2/3: [Dimensionality Reduction & PCA](#class-15-dimensionality-reduction)
2/8: [Recommender Systems](#class-16-recommender-systems) | 2/10: Text Processing / NLP <br>**Peer Feedback on Project Drafts Due**
2/15: **No Class** (President's Day) | 2/17: SQL & Databases <br>**Project Second Draft Due (Optional)**
2/22: Advanced Topic or Guest Speaker | 2/24: Course Review & Where to Go from Here |
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
* For more on cross-validation, read section 5.1 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) (11 pages)
* For another explanation of training error versus testing error, the bias-variance tradeoff, and train/test split (also known as the "validation set approach"), watch Hastie and Tibshirani's video on [estimating prediction error](https://www.youtube.com/watch?v=_2ij6eaaSl0&t=2m34s) (12 minutes, starting at 2:34).
* Caltech's Learning From Data course includes a fantastic video on [visualizing bias and variance](http://work.caltech.edu/library/081.html) (15 minutes).
* [Random Test/Train Split is Not Always Enough](http://www.win-vector.com/blog/2015/01/random-testtrain-split-is-not-always-enough/) explains why random train/test split may not be a suitable model evaluation procedure if your data has a significant time element.

**Additional Resources:**
* [What I do when I get a new data set as told through tweets](http://simplystatistics.org/2014/06/13/what-i-do-when-i-get-a-new-data-set-as-told-through-tweets/) is a fun (yet enlightening) look at the process of exploratory data analysis.

-----

### Class 6: Regression and Regularization

* Regression: Linear, Multiple, Polynomial ([slides](slides/06_regression.pdf))
* Regularization ([slides](slides/06_regression.pdf))

**Resources:**
* Setosa has an excellent [interactive visualization](http://setosa.io/ev/ordinary-least-squares-regression/) of linear regression.
* To go much more in-depth on linear regression, read Chapter 3 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/), from which this lesson was adapted. Alternatively, watch the [related videos](http://www.dataschool.io/15-hours-of-expert-machine-learning-videos/) or read my [quick reference guide](http://www.dataschool.io/applying-and-interpreting-linear-regression/) to the key points in that chapter.
* To learn more about Statsmodels and how to interpret the output, DataRobot has some decent posts on [simple linear regression](http://www.datarobot.com/blog/ordinary-least-squares-in-python/) and [multiple linear regression](http://www.datarobot.com/blog/multiple-regression-using-statsmodels/).
* This [introduction to linear regression](http://people.duke.edu/~rnau/regintro.htm) is much more detailed and mathematically thorough, and includes lots of good advice.
* This is a relatively quick post on the [assumptions of linear regression](http://pareonline.net/getvn.asp?n=2&v=8).
* John Rauser's talk on [Statistics Without the Agonizing Pain](https://www.youtube.com/watch?v=5Dnw46eC-0o) (12 minutes) gives a great explanation of how the null hypothesis is rejected.

-----

### Class 7: Logistic Regression

* Logistic Regression ([slides](slides/07-logistic-regression.pdf))
* Lab: Logistic Regression ([notebook](labs/07-Logistic_Regression.ipynb))

**To Go Deeper**
* Read these excellent articles from BetterExplained: [An Intuitive Guide To Exponential Functions & e](http://betterexplained.com/articles/an-intuitive-guide-to-exponential-functions-e/) and [Demystifying the Natural Logarithm (ln)](http://betterexplained.com/articles/demystifying-the-natural-logarithm-ln/).

**Resources:**
* To go deeper into logistic regression, read the first three sections of Chapter 4 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/).
* For a math-ier explanation of logistic regression, watch the first seven videos (71 minutes) from week 3 of Andrew Ng's [machine learning course](https://www.coursera.org/learn/machine-learning/home/info), or read the [related lecture notes](http://www.holehouse.org/mlclass/06_Logistic_Regression.html) compiled by a student.
* For more on interpreting logistic regression coefficients, read this excellent [guide](http://www.ats.ucla.edu/stat/mult_pkg/faq/general/odds_ratio.htm) by UCLA's IDRE and these [lecture notes](http://www.unm.edu/~schrader/biostat/bio2/Spr06/lec11.pdf) from the University of New Mexico.
* The scikit-learn documentation has a nice [explanation](http://scikit-learn.org/stable/modules/calibration.html) of what it means for a predicted probability to be calibrated.

-----

### Class 8: Naive Bayes

* Naive Bayes ([slides](slides/08-naive-bayes.pdf))
* Lab: Logistic Regression ([notebook](labs/08-Naive_Bayes_Instructor.ipynb))

**Resources:**
* For more on conditional probability, read these [slides](https://docs.google.com/presentation/d/1psUIyig6OxHQngGEHr3TMkCvhdLInnKnclQoNUr4G4U/edit#slide=id.gfc69f484_00), or read section 2.2 of the [OpenIntro Statistics textbook](https://www.openintro.org/stat/textbook.php) (14 pages).
* For an intuitive explanation of Naive Bayes classification, read this post on [airport security](http://www.quora.com/In-laymans-terms-how-does-Naive-Bayes-work/answer/Konstantin-Tt).
* For more details on Naive Bayes classification, Wikipedia has two excellent articles ([Naive Bayes classifier](http://en.wikipedia.org/wiki/Naive_Bayes_classifier) and [Naive Bayes spam filtering](http://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering)), and Cross Validated has a good [Q&A](http://stats.stackexchange.com/questions/21822/understanding-naive-bayes).
* When applying Naive Bayes classification to a dataset with continuous features, it is best to use [GaussianNB](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) rather than [MultinomialNB](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html). Wikipedia has a short [description](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Gaussian_naive_Bayes) of Gaussian Naive Bayes, as well as an excellent [example](https://en.wikipedia.org/wiki/Naive_Bayes_classifier#Sex_classification) of its usage.
* These [slides](http://www.umiacs.umd.edu/~jbg/teaching/DATA_DIGGING/lecture_05.pdf) from the University of Maryland provide more mathematical details on both logistic regression and Naive Bayes, and also explain how Naive Bayes is actually a "special case" of logistic regression.
* Andrew Ng has a [paper](https://cs.stanford.edu/people/ang//papers/nips01-discriminativegenerative.pdf) comparing the performance of logistic regression and Naive Bayes across a variety of datasets.
* If you enjoyed Paul Graham's article, you can read [his follow-up article](http://www.paulgraham.com/better.html) on how he improved his spam filter and this [related paper](http://www.merl.com/publications/docs/TR2004-091.pdf) about state-of-the-art spam filtering in 2004.

-----

### Class 9: Clustering

* Clustering ([slides](slides/09-clustering.pdf)
	* K-means: [visualiztion](http://tech.nitoyon.com/en/blog/2013/11/07/k-means/)
    * K-means: [visualization](http://www.naftaliharris.com/blog/visualizing-k-means-clustering/)
    * DBSCAN: [visualization](http://www.naftaliharris.com/blog/visualizing-dbscan-clustering/)
* Lab: K-Means ([notebook](labs/09-KMeans.ipynb))

**Clustering Resources:**
* scikit-learn's documentation on [clustering](http://scikit-learn.org/stable/modules/clustering.html) compares many different types of clustering.
* For a very thorough introduction to clustering, read chapter 8 (69 pages) of [Introduction to Data Mining](http://www-users.cs.umn.edu/~kumar/dmbook/index.php) (available as a free download), or browse through the chapter 8 slides.
* An Introduction to Statistical Learning has useful videos on [K-means clustering](https://www.youtube.com/watch?v=aIybuNt9ps4&list=PL5-da3qGB5IBC-MneTc9oBZz0C6kNJ-f2) (17 minutes) and [hierarchical clustering](https://www.youtube.com/watch?v=Tuuc9Y06tAc&list=PL5-da3qGB5IBC-MneTc9oBZz0C6kNJ-f2) (15 minutes).
* Fun examples of clustering: [A Statistical Analysis of the Work of Bob Ross](http://fivethirtyeight.com/features/a-statistical-analysis-of-the-work-of-bob-ross/) (with [data and Python code](https://github.com/fivethirtyeight/data/tree/master/bob-ross)), [How a Math Genius Hacked OkCupid to Find True Love](http://www.wired.com/2014/01/how-to-hack-okcupid/all/), and [characteristics of your zip code](http://www.esri.com/landing-pages/tapestry/).

-----

### Class 10: APIs & Web Scraping

* Web APIs ([slides](slides/10-apis-scraping.pdf))
* Lab: Web Scraping by Dave Yerrington ([notebook](labs/10_Web_Scraping.ipynb))

**API Resources:**
* [Mashape](https://www.mashape.com/explore) and [Apigee](https://apigee.com/providers) allow you to explore tons of different APIs. Alternatively, a [Python API wrapper](http://www.pythonforbeginners.com/api/list-of-python-apis) is available for many popular APIs.
* [API Integration in Python](https://realpython.com/blog/python/api-integration-in-python/) provides a very readable introduction to REST APIs.
* Microsoft's [Face Detection API](https://www.projectoxford.ai/demo/face#detection), which powers [How-Old.net](http://how-old.net/), is a great example of how a machine learning API can be leveraged to produce a compelling web application.

**Web Scraping Resources:**
* The [Beautiful Soup documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) is incredibly thorough, but is hard to use as a reference guide. However, the section on [specifying a parser](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#specifying-the-parser-to-use) may be helpful if Beautiful Soup appears to be parsing a page incorrectly.
* For more Beautiful Soup examples and tutorials, see [Web Scraping 101 with Python](http://www.gregreda.com/2013/03/03/web-scraping-101-with-python/), Alex's well-commented notebook on [scraping Craigslist](http://nbviewer.ipython.org/github/Alexjmsherman/DataScience_GeneralAssembly/blob/master/Final_Project/1.%20Final_Project_Data%20Scraping.ipynb), this [notebook](http://web.stanford.edu/~zlotnick/TextAsData/Web_Scraping_with_Beautiful_Soup.html) from Stanford's Text As Data course, and this [notebook](http://nbviewer.ipython.org/github/cs109/2014/blob/master/lectures/2014_09_23-lecture/data_scraping_transcript.ipynb) and associated [video](http://cm.dce.harvard.edu/2015/01/14328/L07/screen_H264LargeTalkingHead-16x9.shtml) from Harvard's Data Science course.
* For a much longer web scraping tutorial covering Beautiful Soup, lxml, XPath, and Selenium, watch [Web Scraping with Python](https://www.youtube.com/watch?v=p1iX0uxM1w8) (3 hours 23 minutes) from PyCon 2014. The [slides](https://docs.google.com/presentation/d/1uHM_esB13VuSf7O1ScGueisnrtu-6usGFD3fs4z5YCE/edit#slide=id.p) and [code](https://github.com/kjam/python-web-scraping-tutorial) are also available.
* For more complex web scraping projects, [Scrapy](http://scrapy.org/) is a popular application framework that works with Python. It has excellent [documentation](http://doc.scrapy.org/en/1.0/index.html), and here's a [tutorial](https://github.com/rdempsey/ddl-data-wrangling) with detailed slides and code.
* [robotstxt.org](http://www.robotstxt.org/robotstxt.html) has a concise explanation of how to write (and read) the `robots.txt` file.
* [import.io](https://import.io/) and [Kimono](https://www.kimonolabs.com/) claim to allow you to scrape websites without writing any code.
* [How a Math Genius Hacked OkCupid to Find True Love](http://www.wired.com/2014/01/how-to-hack-okcupid/all/) and [How Netflix Reverse Engineered Hollywood](http://www.theatlantic.com/technology/archive/2014/01/how-netflix-reverse-engineered-hollywood/282679/?single_page=true) are two fun examples of how web scraping has been used to build interesting datasets.


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

**Other Resources:**
* scikit-learn has extensive documentation on [model evaluation](http://scikit-learn.org/stable/modules/model_evaluation.html).
* Section 3.3.1 of [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/) (4 pages) has a great explanation of dummy encoding for categorical features.

-----

### Class 12: Decision Trees

* Decision Trees for Classification ([slides](slides/12-decision-trees.pdf))
* Lab: Decision Trees ([notebook](labs/12-Classification_Trees.ipynb))

**Resources:**
* scikit-learn's documentation on [decision trees](http://scikit-learn.org/stable/modules/tree.html) includes a nice overview of trees as well as tips for proper usage.
* For a more thorough introduction to decision trees, read section 4.3 (23 pages) of [Introduction to Data Mining](http://www-users.cs.umn.edu/~kumar/dmbook/index.php). (Chapter 4 is available as a free download.)
* This paper, [The Science of Singing Along](http://www.doc.gold.ac.uk/~mas03dm/papers/PawleyMullensiefen_Singalong_2012.pdf), contains a neat regression tree for predicting the percentage of an audience at a music venue that will sing along to a pop song.
* If you want to go deep into the different decision tree algorithms, this slide deck contains [A Brief History of Classification and Regression Trees](https://drive.google.com/file/d/0B-BKohKl-jUYQ3RpMEF0OGRUU3RHVGpHY203NFd3Z19Nc1ZF/view).

**Installing GraphViz (optional):**
* Mac: [Download and install PKG file](http://www.graphviz.org/Download_macos.php)
* Windows: [Download and install MSI file](http://www.graphviz.org/Download_windows.php), and then add GraphViz to your path:
    * Go to Control Panel, System, Advanced System Settings, Environment Variables
    * Under system variables, edit "Path" to include the path to the "bin" folder, such as: `C:\Program Files (x86)\Graphviz2.38\bin`

-----

### Class 13: Ensembles and Random Forests

* Ensemble Methods & Random Forests ([slides](slides/13-ensemble-methods-random-forests.pdf))
* Lab: Ensemble Methods & Random Forests ([notebook](labs/13-Ensemble_Methods_and_Forests.ipynb))

**Resources:**
* scikit-learn's documentation on [ensemble methods](http://scikit-learn.org/stable/modules/ensemble.html) covers both "averaging methods" (such as bagging and Random Forests) as well as "boosting methods" (such as AdaBoost and Gradient Tree Boosting).
* For an intuitive explanation of Random Forests, read Edwin Chen's answer to [How do random forests work in layman's terms?](http://www.quora.com/Random-Forests/How-do-random-forests-work-in-laymans-terms/answer/Edwin-Chen-1)
* MLWave's [Kaggle Ensembling Guide](http://mlwave.com/kaggle-ensembling-guide/) is very thorough and shows the many different ways that ensembling can take place.

-----

### Class 14: Support Vector Machines

* Support Vector Machines ([slides](slides/14-support-vector-machines.pdf))
* Lab: SVMs: Illuminating Advanced Classifiers ([notebook](labs/14-SVMs.ipynb))

**Additional Resources:**
* See the video embedded in the answer to [this question on Quora](https://www.quora.com/What-does-support-vector-machine-SVM-mean-in-laymans-terms) for a great animation of how kernels project non-linear classification problems into a higher dimensional space where they can be solved with a linear decision boundary / maximum margin hyperplane.
* For students who enjoy digging into the underlying mathematical concepts, [this reading](http://www.cs.colostate.edu/%7Easa/pdfs/howto.pdf) details the math behind support vector machines. Some of the examples in the lecture slides are taken from this reading.
* [Supervised learning superstitions cheat sheet](http://ryancompton.net/assets/ml_cheat_sheet/supervised_learning.html) is a very nice comparison of five classifiers we cover in the course (logistic regression, decision trees, KNN, Naive Bayes, and support vector machines).

-----

### Class 15: Dimensionality Reduction

* Dimensionality Reduction ([slides](slides/15-dimensionality-reduction.pdf))
* Lab: Dimensionality Reduction & Principle Components Analysis ([notebook](labs/15-Dimensionality_Reduction.ipynb))

**Additional Resources**
* [This tutorial](http://www.cs.otago.ac.nz/cosc453/student_tutorials/principal_components.pdf) on Principal Components Analysis (PCA) includes good refreshers on covariance and linear algebra
* To go deeper on Singular Value Decomposition, read [Kirk Baker's excellent tutorial](https://www.ling.ohio-state.edu/%7Ekbaker/pubs/Singular_Value_Decomposition_Tutorial.pdf).

-----

### Class 16: Recommender Systems

Thanks to Dave Yerrington for leading this session!

* Recommendation Engines ([slides](slides/16-recommendation_engines.pdf))
* Lab: Similar Users Recommender Lab ([notebook](labs/16-Similar_Users_Recommender_Lab.ipynb))


-----

### Class 17: Text Processing & NLP

-----

### Class 18: Databases & SQL

-----

### Class 19: Advanced Topic or Guest Speaker

**Additional Resources:**
* Browse the excellent [solution paper](https://docs.google.com/viewer?url=https://raw.githubusercontent.com/ChenglongChen/Kaggle_CrowdFlower/master/Doc/Kaggle_CrowdFlower_ChenglongChen.pdf) from the winner of Kaggle's [CrowdFlower competition](https://www.kaggle.com/c/crowdflower-search-relevance) for an example of the work and insight required to win a Kaggle competition.
* [Interpretable vs Powerful Predictive Models: Why We Need Them Both](https://medium.com/@chris_bour/interpretable-vs-powerful-predictive-models-why-we-need-them-both-990340074979) is a short post on how the tactics useful in a Kaggle competition are not always useful in the real world.

-----

### Class 20: Course Review & Where to Go from Here

-----

### Classes 21 and 22: Final Project Presentations

* Project presentations!


