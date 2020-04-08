from setuptools import setup, find_packages


setup(
    name='vkbotfather',
    description='Father for creating VK Bots',
    version='0.1.2',
    url='https://github.com/wultes/vkbotfather',
    license='MIT',
    author='Wultes (Kirill)',
    author_email='wultesu@gmail.com',
    packages=['vkbotfather', 'vkbotfather.fatherbot', 'vkbotfather.fatherbot', 'vkbotfather.fatherbot.models', 'vkbotfather.utils'],
    install_requires=['toml', 'Pillow']
)
