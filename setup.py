from __future__ import absolute_import

from setuptools import setup, find_packages

install_deps = [
    'ansible-vault==2.1.0',
    'ansible~=4.3',
    'ansible-inventory==0.6.4',
    'argparse>=1.4',
    'attrs>=18.1.0',
    'boto3>=1.9.131',
    'clint',
    'couchdb-cluster-admin',
    'cryptography~=38.0',
    'datadog>=0.2.0',
    'dimagi-memoized>=1.1.0',
    'dnspython',
    'Fabric3>=1.10.2,<1.11',
    # can remove once requests bumps its version requirement
    # https://github.com/requests/requests/issues/4681
    'idna==2.6',
    'importlib-metadata==3.1.0',
    'jinja2-cli',
    'jsonobject',
    'netaddr',
    'passlib',
    'pycryptodome>=3.6.6',  # security update
    'PyGithub>=1.43.3',
    'pyOpenSSL~=22.0',
    'pytz',
    'simplejson',
    'six',
    'tabulate'
]
test_deps = [
    'modernize',
    'nose @ git+https://github.com/dimagi/nose.git@06dff28bbe661b9d032ce839ea0ec8e9eaf6f337',
    'parameterized>=0.6.1',
    'requests-mock',
]
aws_deps = [
    'awscli',
]
extras = {
    'test': test_deps,
    'aws': aws_deps,
}

setup(
    name='commcare-cloud',
    description="A tool for managing commcare deploys.",
    long_description="",
    license='BSD-3',
    include_package_data=True,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'commcare-cloud = commcare_cloud.commcare_cloud:main',
            'cchq = commcare_cloud.commcare_cloud:main',
            'manage-commcare-cloud = commcare_cloud.manage_commcare_cloud.manage_commcare_cloud:main',
            'patched-fab = commcare_cloud.patched_fab:main',
        ],
    },
    install_requires=install_deps,
    tests_require=test_deps,
    extras_require=extras,
)
