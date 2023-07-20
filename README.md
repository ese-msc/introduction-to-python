# Introduction to Python

Welcome to **Introduction to Python**! Python is one of the most popular and powerful programming languages. It is used extensively in computational and data science, and you will use it in almost all modules during your MSc studies. This self-guided course will help you to learn the basics of Python.

This course consists of four lectures (1, 2, 3, and 4), and we strongly recommend completing them in that order.

## How to run this course

There are three possibilities for how you can learn Python with our self-guided course. **JupyterHub** and **Binder** options allow you to run tutorials in the cloud - you do not need to install anything, and no files will be created on your machine. All you need is a web browser and internet connection. However, you need to download Jupyter notebooks you worked in to ensure your work is not lost at the end of each session. The third option is to create a Python environment and run all tutorials on your machine. There is no difference in what you will learn, and we give you complete freedom to choose how you want to run tutorials.

### 1. JupyterHub (ESE students)

1. **Create a GitHub account**. In the email you received, we sent you your unique username. Create a GitHub account and make sure your GitHub account uses that username.

2. **Login to JupyterHub**. By clicking the following badge, you can access our JupyterHub server and log in using the GitHub account you just created:

[![JupyterHub](https://img.shields.io/badge/JupyterHub-ese--msc-orange)](https://ese-jhub-pre-sess.westeurope.cloudapp.azure.com/pre-sess/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fese-msc%2Fintroduction-to-python&urlpath=lab%2Ftree%2Fintroduction-to-python%2F&branch=main)

After login, it may take some time for JupyterHub to start for the first time, so please be patient.

**IMPORTANT:** Please note that we do not guarantee your work is backed up. Therefore, we strongly recommend downloading the notebook at the end of each session.

### 2. Binder

You can access Binder by clicking on the *Binder badge*:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ese-msc/introduction-to-python/HEAD?labpath=index.ipynb)

**IMPORTANT:** Please note that after the Binder session ends, all your work is deleted. Therefore, please download the notebook you worked in at the end of each session.

### 3. On your machine

1. **Install Git**. Please follow installation instructions for your operating system on [Git webpage](https://git-scm.com/).

2. **Clone repository**. In Terminal (Linux and MacOS) or Command Prompt (Windows), navigate to the location where you want the course files to be and run
```console
$ git clone https://github.com/ese-msc/introduction-to-python
```    
3. **Install Anaconda**. We recommend installation using conda package manager. If you do not already have it installed, download [Anaconda](https://www.anaconda.com/products/individual) Python 3 for your operating system and follow the instructions to install it. After the installation is complete, in Terminal (Linux and MacOS) or Anaconda Prompt (Windows), navigate to the course directory, create a new conda environment, and activate it:
```console
$ cd path/to/course/directory
$ conda env create -f environment.yml
$ conda activate introduction-to-python
``` 
4. **Open Jupyter Notebook**. In the environment you just activated, run:
```console
$ jupyter notebook &
```

## Testing

After (almost) each exercise, there are two cells containing some code. In those cells, we test your solution using two different methods:

1. **PyBryt** analyses your solution and provides you feedback on what is correct in your implementation, as well as what might be wrong. Please read PyBryt's feedback carefully and address the `ERROR` messages by modifying your solution.
2. **assert** statements validate your final solution

It is important to follow the instructions for each exercise exactly and do not change the names of variables, functions, or classes so that tests can analyse your code. Besides, please do not change the content of any of the testing cells.

Although **PyBryt** provides much more detailed feedback, it is possible it complains about your code even though **assert** statement confirms your code is correct. This is because PyBryt testing is based on comparing your solution to reference solutions. Since there is virtually an infinite number of alternative solutions, it is possible that your solution is not in our references. On the other hand, assert statements check the final result of your code and if they do not raise an error, your code is correct and you do not have to address **PyBryt**'s error messages (if any).

## Support

**We encourage questions!** If you require support, have questions, want to report a bug, or want to suggest an improvement, please raise an issue in the [course repository](https://github.com/ese-msc/introduction-to-python).

> **Q:** I don't know where to ask my question. It might be related to something else, but I'm unsure. What should I do?  
> **A:** Open an issue in this repository. This is a safe, respectful space to ask questions and open issues.

> **Q:** I've never opened an issue. How do I do it?  
> **A:** Click the `Issues` tab next to top of the page, then click the green `New Issue` button. Ask your question in the title and comment fields, then click  `Submit new issue`. Congratulations, you submitted your question! We will try to get back to you shortly.

> **Q:** How can I see if somebody else had the same or similar question?  
> **A:** When you click the `Issues` tab next to top of the page, you can see all issues that are currently open and are being addressed. In addition to them, you can also check the issues that have been resolved in [closed issues](https://github.com/ese-msc/introduction-to-python/issues?q=is%3Aissue+is%3Aclosed).

Are you a community member that enjoys sharing your knowledge and helping others solve problems? We encourage you to respond to these issues.