from setuptools import find_packages, setup

package_name = 'talker_listner'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nchougul',
    maintainer_email='chougulenikhil88@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talkerNode = talker_listner.talker_node:main'
            'listnerNode = talker_listner.listner_node:main'
            
        ],
    },
)
