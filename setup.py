from setuptools import setup, find_packages


setup(
    name='vkbotfather',
    description='Father for creating VK Bots',
    version='0.1.6',
    url='https://github.com/wultes/vkbotfather',
    license='MIT',
    author='Wultes (Kirill)',
    author_email='wultesu@gmail.com',
    packages=['vkbotfather', 'vkbotfather.fatherbot', 'vkbotfather.fatherbot', 'vkbotfather.fatherbot.models', 'vkbotfather.utils', 'vkbotfather.plugins'],
    install_requires=['toml', 'Pillow']
)
