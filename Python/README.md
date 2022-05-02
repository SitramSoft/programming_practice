# **Repository used for tracking my journey in learning Python programming language**

## **Progress**

### 02.05.2022

* [languageSummary](languageSummary.md) file created with a summary of Python synthax.
* fixed markdown lint warnings.

### 07.04.2021

* Learned about web scrapping with [Selenium](https://www.selenium.dev/documentation/en/getting_started/) and a webdriver for chrome. This can be done in a headless environment, like the Ubuntu server where I do most of my development but best is to run it in a desktop environment.

### 13.03.2021

* First concept in chapter 4 is about mean squared error. It's a good thing to square an error, because it makes small errors smaller and big errors bigger.
* page 54

### 07.03.2021

* The book makes reference to [NumPy](https://numpy.org/doc/stable/user/index.html). I started to read the User Guide available on the website to try and get a quick overview of what the library offers.
* The chapter starts to become difficult to follow. I decided to go trough it at a faster rate without focusing so much on taking detailed notes. Hopefully I will be able to begin building a mental image of neural networks then come back to certain chapters for details.
* Chapter 3 which goes into detail about forward propagation is done.
* I need to go over a few examples of NumPy dot function. I found an easy to understand explanation of dot function on matrices [here](https://www.mathsisfun.com/algebra/matrix-multiplying.html) which is worth to bookmark for the future.
* page 48(started chapter 4)

### 06.03.2021

* Learned about weighted sum network
* The interface for a neural network is simple. It accepts as inputs a list of information and a weights as knowledge. It outputs a prediction based on the inpus.
* Page 34

### 17.02.2021

* The neural network outputs a prediction based on the input and the weight.
* Th network can give false predictions then it should try to adjust the weights in order to predict more accurately the next time it sees the same input
* Implementing a simple neural network with a single node
* Network sensitivity is related to the weight. If the weight is very high then even the tiniest input can create a large variation in prediction.
* page 27

### 16.02.2021

* Created support for solving challenged from [Hackarrank.com](https://www.hackerrank.com/dashboard) in python. No solutions yet added to the repo
* I found an interesting series on [bdtechtalks](https://bdtechtalks.com/) called [AI education](https://bdtechtalks.com/tag/ai-education/). [First article](https://bdtechtalks.com/2021/02/10/grokking-deep-learning-review/) in the series contains a promising approach in self studying Deep Learning using Andrew Trusk [Grokking Deep Learning](https://www.amazon.com/Grokking-Deep-Learning-Andrew-Trask/dp/1617293709) book. The article mentions that this book doesn't need a strong mathematical background in linear algebra and calculus to start learning this field. I decided to give the book a try and see how long before I loose interest in it.
* So far the book promises to provide an easy approach in teaching what deep learning is which will prepare me for learning one of the existing frameworks(Torch, TensorFlow, Keras and others)
* 90% of the projects I start, something doesn't work from the first step. In this case, I get a "The folder you are executing pip from can no longer be found." when trying to install numpy with pip. I guess I'm going to start debugging this and by the time I'm done with it I will need a break from the mental exhaustion :(
* That was easy :) Apparently I run the commands from a directory that I deleted and that's why I was getting the error above. Next step is to figure out if I need [Jupyter Notebook](https://jupyter.org/) or I can code on my code-server instance in plain Python without additional support.
* It takes too much time to understand the benefits of [Jupyter Notebook](https://jupyter.org/) so I decided to not use it for now. Hopefully I won't regret it later on. Finally I can get back to the book.
* Deep learning is a subset of methods in machine learning toolbox, primarily using artificial neural networks inspired by the human brain
* **Supervised vs unsupervised** learning -> this is about the _type of pattern_ being learned
* **Supervised learning** is the direct imitation of a pattern between two datasets. **What you know -> supervised learning -> what you want to know**
* **Unsupervised learning** transforms one data set into another, _which is not previously known or understood_
* **Parametric vs nonparametric** -> this is about the _method for learning_
* **Parametric learning** is characterized by having a fixed number of parameters
* **Nonparametric model** is characterized by having an infinite number of parameters, determined by data
* Page 44

### 13.10.2020

* Reworked the existing python files because they were not compiling with with python 3
* Practiced a bit Markdown syntax by reworking the README.md file in the repository in order to keep a status of activities done. This way it's easier to remember where I left in case I need to take a break and resume this activity later on. Found a great [reference](https://www.markdownguide.org/basic-syntax/) online for quickly checking different syntax elements
* Started going trough [Automate the Boring Stuff with Python chapter 8](https://automatetheboringstuff.com/2e/chapter8/)

### 14.10.2020

* Continue going trough [Automate the Boring Stuff with Python chapter 8](https://automatetheboringstuff.com/2e/chapter8/)

### 19.10.2020

* Found a new repo on GitHub name [Practical Python](https://github.com/dabeaz-course/practical-python/blob/master/Notes/Contents.md) which seems to be worth going trough since it offers a more compact organization of information. Decided to set on hold the current course and continue with this one.
* Organized the files in the repo based on the different course or library that I study. So far all the scripts are split into 3 categories:
  * [Automate the Boring Stuff with Python](https://github.com/SitramSoft/pythonLearning/tree/master/Automate%20the%20Boring%20Stuff%20with%20Python) - contains scripts created while going trough the [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/2e/) course
  * [Others](https://github.com/SitramSoft/pythonLearning/tree/master/Other) - contains misc scripts from unknown courses
  * [PyGame](https://github.com/SitramSoft/pythonLearning/tree/master/PyGame) - contains  scripts used for learning the [PyGame library](https://www.pygame.org/news)
  * Practical Python Programming - contains scripts created while going trough the [Practical Python Programming](https://github.com/dabeaz-course/practical-python) course from GitHub
