from setuptools import setup, find_packages

setup(
    name="intelligent_doc_ocr",
    version="16.0.0",
    description="Frappe v16 Intelligent Document Processing & OCR Extractor - Official Frappe & ERPNext v16 App",
    author="Shyamkumar Pandey",
    author_email="shyampandey1104@gmail.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=["frappe"]
)
