from glob import glob
import setuptools

setuptools.setup(
    name="{{ cookiecutter.extension_name }}",
    version='0.0.0',
    url="{{ cookiecutter.repository }}",
    author="{{ cookiecutter.author_name }}",
    description="{{ cookiecutter.project_short_description }}",
    packages=setuptools.find_packages(),
    install_requires=[
        'notebook',
    ],
    zip_safe=False,
    include_package_data=True
)