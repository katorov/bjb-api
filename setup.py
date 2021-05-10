from setuptools import setup, find_packages

setup(
    name='BabyJournalBot Async API',
    version='1.0',
    description='Async client API used across BabyJournalBot project',
    author_email='katorov.msu@gmail.com',
    python_requires='>=3.8.0',
    packages=find_packages(),
    install_requires=[
      'aiohttp>=3.7.4.post0',
      'requests',
    ],
)
