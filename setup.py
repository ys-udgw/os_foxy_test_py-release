from setuptools import setup

package_name = 'ros_foxy_test_py'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules=[
        'test_pub/test_publisher'
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='hogehoge',
    author_email='hoge@example.com',
    maintainer='hogehogee',
    maintainer_email='hoge@example.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Examples of minimal publishers using rclpy.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test = test_pub.test_publisher:main',
        ],
    },
)
