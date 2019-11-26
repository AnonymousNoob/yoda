import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='yoda',  
     version='0.1',
     scripts=['yoda'] ,
     author="Praveen M",
     author_email="praveenmxy@gmail.com",
     description="A Self Manged lightweight Repo Manager",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/AnonymousNoob/yoda",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )