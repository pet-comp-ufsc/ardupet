import setuptools

setuptools.setup(
		name='Ardupet',
		version='0.0.1-alpha',
		description='Python communication with Arduino board for office automation',
		url='https://github.com/ranisalt/ardupet',
		author='Ranieri Althoff',
		author_email='ranisalt@gmail.com',
		license='MIT',
		install_requires=['flask', 'pyserial'],
)
