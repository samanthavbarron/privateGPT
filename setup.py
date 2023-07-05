import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="privateGPT",
    description="privateGPT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/imartinez/privateGPT",
    packages=["privateGPT"],
    install_requires=[
        "langchain==0.0.197",
        "gpt4all==0.3.4",
        "chromadb==0.3.23",
        "llama-cpp-python==0.1.50",
        "urllib3==2.0.2",
        "PyMuPDF==1.22.3",
        "python-dotenv==1.0.0",
        "unstructured==0.6.6",
        "extract-msg==0.41.1",
        "tabulate==0.9.0",
        "pandoc==2.3",
        "pypandoc==1.11",
        "tqdm==4.65.0",
    ]
)
