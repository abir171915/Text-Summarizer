import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "abir171915"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "abirfarabi915@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "A small python project"
    long_description = long_description,
)