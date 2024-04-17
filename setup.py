import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='subete_ga_F_ni_naru',
    version='0.0.1',
    author='howsmyanimeprofilepicture',
    author_email='howsmyanimeprofilepicture@gmail.com',
    description='functools-like library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/howsmyanimeprofilepicture/Subete-ga-F-ni-Naru',
    project_urls = {
        "Bug Tracker": "https://github.com/howsmyanimeprofilepicture/Subete-ga-F-ni-Naru/issues"
    },
    license='MIT',
    packages=['Subete-ga-F-ni-Naru'], 
    install_requires=[],
)
