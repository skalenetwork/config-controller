#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)

extras_require = {
    'linter': [
        "flake8==3.7.9"
    ],
    'dev': [
        "twine==3.1.1"
    ],
}

extras_require['dev'] = (
    extras_require['linter'] + extras_require['dev']
)

setup(
    name='deploy-controller-predeployed',
    version='1.0.0',
    description='A tool for generating predeployed deploy controller smart contract',
    long_description_markdown_filename='README.md',
    author='SKALE Labs',
    author_email='support@skalelabs.com',
    url='https://github.com/skalenetwork/deploy-controller',
    install_requires=[
        "predeployed-generator == 0.0.1a2"
    ],
    python_requires='>=3.7,<4',
    extras_require=extras_require,
    keywords=['skale', 'predeployed'],
    packages=find_packages(),
    package_data={
        'deploy_controller_predeployed': ['artifacts/DeployController.json']
    },
    setup_requires=["setuptools-markdown"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ]
)