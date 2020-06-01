from setuptools import setup, find_packages


setup(
    name='vkbotfather',
    description='Father for creating VK Bots',
    version='0.3.0',
    url='https://github.com/wultes/vkbotfather',
    license='MIT',
    author='Wultes (Kirill)',
    author_email='wultesu@gmail.com',
    packages=find_packages(),
    install_requires=['toml', 'Pillow', 'requests'],
)
