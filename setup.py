from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

long_description = long_description.replace('assets/imgs/demo1.png',"https://github.com/SivaSankarS365/Markdown-code-runner/raw/main/assets/imgs/demo1.png")
long_description = long_description.replace('assets/imgs/demo2.png',"https://github.com/SivaSankarS365/Markdown-code-runner/raw/main/assets/imgs/demo2.png")
long_description = long_description.replace('assets/imgs/timeit.png',"https://github.com/SivaSankarS365/Markdown-code-runner/raw/main/assets/imgs/timeit.png")

setup(
    name='mdcoderunner',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'jinja2==3.1.2',
    ],
    entry_points={
        'console_scripts': ['mdcoderunner=mdcoderunner.mdcoderunner:main']
    },
    author='Siva Sankar Sajeev',
    author_email='sivasankars365@gmail.com',
    description='A tool for preparing for technical interviews, particularly for learning Data Structures and Algorithms (DSA).',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SivaSankarS365/Markdown-code-runner',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)