from setuptools import find_packages, setup

setup(name= "agentic-ai-planner",
      version= "0.0.1",
      author = "Shithil",
      author_email= "shithilrbirthi@gmail.com",
      packages= find_packages(),
      install_requires = ['langchain-astradb', 'langchain'])