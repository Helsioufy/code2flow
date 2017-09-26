from setuptools import setup, find_packages
setup(
	name='code2flow',
	version='0.2',
	description='Visualize your source code as DOT flowcharts',
	long_description=open('README.md').read(),
	scripts=['code2flow'],
	package_dir={'code2flowlib': 'code2flowlib'},
	license='LGPL',
	author='Hany Elsioufy',
	author_email='helsioufy@smartec-group.com',
	url='https://github.com/Helsioufy/code2flow',
	packages=find_packages(),
	classifiers = (
		'Natural Language :: English',
		'Programming Language :: Python',
		)
	)
