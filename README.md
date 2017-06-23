## Speech Recognition Class for generating Cisco Zeus Metric Query

### 1. Dependencies

Speech recognition engine used is CMU Sphinx
https://cmusphinx.github.io/
Libraries installed from CMU Sphinx
*pocketsphinx*  
*sphinxbase*

for reference  on installing CMU Sphinx see  

_http://depado.markdownblog.com/2015-05-13-tutorial-on-pocketsphinx-with-python-3-4_


**Other python libraries required**

*pyaudio  
portaudio  
wave  
audioop  
collections  
time  
math*  

All the above can be installed using

`pip3 install <package Name>`

### 2. Working

The python program first tests the Mic intensity for a threshold. Gives a warning if lower than a threshold.
Then it listens to the audio input (meant to be a query) and outputs a sequence of words which it recognizes.

Comment on accuracy and further work

Works well with clean audio with some mistakes where the words can be ambiguous.


