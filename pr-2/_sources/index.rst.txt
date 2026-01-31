================================
Sphinx Revealjs with Stlite Demo
================================

.. revealjs-section::

Introduction
============

Welcome to Sphinx Revealjs with Stlite!

This presentation demonstrates:

* Sphinx Revealjs for slides
* Stlite for interactive Python
* GitHub Pages deployment
* PR preview functionality

.. revealjs-break::

What is Sphinx Revealjs?
=========================

Sphinx Revealjs is a Sphinx extension that allows you to create beautiful HTML presentations using Reveal.js.

Features:

* Write slides in reStructuredText
* Easy to maintain with Sphinx
* Beautiful transitions
* Responsive design

.. revealjs-break::

What is Stlite?
===============

Stlite is a Python runtime that runs entirely in the browser using WebAssembly.

Key benefits:

* No server required
* Interactive Python code
* Streamlit compatibility
* Works offline

.. revealjs-break::

Interactive Python Demo
=======================

.. stlite::

   import streamlit as st
   import pandas as pd

   st.title("Interactive Data Demo")
   
   # Create a simple dataframe
   df = pd.DataFrame({
       'first column': [1, 2, 3, 4],
       'second column': [10, 20, 30, 40]
   })
   
   st.write("Here's our first attempt at using data:")
   st.write(df)

.. revealjs-break::

User Input Example
==================

.. stlite::

   import streamlit as st
   
   name = st.text_input('Your name')
   st.write(f'Hello, {name or "world"}!')

.. revealjs-break::

Interactive Chart
=================

.. stlite::
   :requirements: matplotlib

   import streamlit as st
   import matplotlib.pyplot as plt
   import numpy as np

   size = st.slider("Sample size", 100, 1000)
   arr = np.random.normal(1, 1, size=size)
   fig, ax = plt.subplots()
   ax.hist(arr, bins=20)
   st.pyplot(fig)

.. revealjs-break::

GitHub Pages Deployment
========================

This presentation is automatically deployed to GitHub Pages using GitHub Actions.

Workflow:

1. Push to main branch
2. GitHub Actions builds the slides
3. Deployed to GitHub Pages
4. Available at your-repo.github.io

.. revealjs-break::

PR Preview Feature
==================

Pull requests automatically generate preview deployments!

Benefits:

* Review changes before merging
* Share previews with team
* Test in production-like environment
* Automatic cleanup after merge

.. revealjs-break::

How It Works
============

PR Preview Process:

1. Open a pull request
2. GitHub Actions builds preview
3. Deploys to ``gh-pages`` branch with PR prefix
4. Comment added with preview URL
5. Preview auto-removed when PR closes

.. revealjs-break::

Getting Started
===============

To use this template:

.. code-block:: bash

   # Clone the repository
   git clone your-repo-url
   
   # Install dependencies
   pip install -e .
   
   # Build slides
   sphinx-build -b revealjs source build
   
   # Open build/index.html

.. revealjs-break::

Customization
=============

Edit ``source/conf.py`` to customize:

* Theme (black, white, league, sky, etc.)
* Transitions (slide, fade, convex, etc.)
* Controls and navigation
* Plugins and extensions

.. revealjs-break::

Adding Content
==============

Create new slides with:

.. code-block:: rst

   .. revealjs-break::
   
   Your Slide Title
   ================
   
   Your content here

Supports:

* Images, code blocks, tables
* Math equations
* Custom HTML
* Embedded content

.. revealjs-break::

Thank You!
==========

Questions?

----

Repository: https://github.com/tkoyama010/awesome-sphinx-revealjs

Documentation: https://sphinx-revealjs.readthedocs.io/
