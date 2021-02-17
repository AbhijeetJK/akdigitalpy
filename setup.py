from distutils.core import setup


setup(
  name = 'akdigitalpy',        
  packages = ['akdigitalpy'],   
  version = '1.0',      
  license='MIT',              
description = 'liabrary to conversion of digital number system and calculate complement',   
  author = 'Abhijeet Khatri',                   
  author_email = 'abhijeetkhatri@gmail.com',      
  url = 'https://github.com/AbhijeetJK/akdigitalpy.git',
download_url ='https://github.com/AbhijeetJK/akdigitalpy/archive/1.0.0.tar.gz',  
  keywords = ['ditalpy', 'Binary', 'Decimal','Octal','Hexadecimal','Complement'],   
  install_requires=[            
          'akdigitalpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
