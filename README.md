perapera-frequency
==================

Add word frequency information to your pera-pera kun popup Chinese dictionary.
--------------------------------------------------------------------------------------------------------------

This python program will look in a local corpus and append word frequency descriptions to the end of the pera-pera definitions.

*Note: this only works for firefox at the moment.*





Descriptions of Frequency Levels
---------------------------------------

        200:'very basic',         #1-477                  = 500                         cum 500
        100:'basic',              #477-1016             = 500                          1000
        50:'very common',         #1017-2060           = 1000                        2000
        25:'common',              #2060-3760           = 1700                        3700
        13:'uncommon',            #3760-6313          = 2600                        6300
        7:'rare',                 #6300-10050         = 3750                        10000
        2:'very rare',            #10500-18600        = 8100                        18000
        0:'obscure'}              #18600-50000        = 31400                      50000
        
        
I picked these after some experimentation and they can be modified.  For intermediate students, memorizing very rare or obscure words is pretty useless unless it's your field of specialization.

And in general it's not efficient to spend time memorizing words which appear 1 time per million words when there are words that appear 50 times/ mil which you don't know.

![ScreenShot](https://raw.github.com/ernop/perapera-frequency/master/common.png)

![ScreenShot](https://raw.github.com/ernop/perapera-frequency/master/veryrare.png)


What is pera pera kun?
-----------------------------------

https://addons.mozilla.org/en-us/firefox/addon/perapera-kun-chinese-popup-tra/ 

It is an awesome add-on for firefox which pops up a definition for chinese words when you mouse-over them.


The corpus
----------------------------
The corpus is compiled from a bunch of internet sources & seems fairly accurate to what I've read.  It's a lot better than the business / news derived ones I've read.


Howto use
-----------------
Download modified-dict.sqlite which already has the frequency descriptions.  

1. close firefox

2. find your firefox folder something like ```c:\users\<username>\AppData\Roaming\Mozilla\Firefox\Profiles\<random name>.default\extensions\chineseperakun@gmail.com```

3. copy the modified-dict.sqlite file in there

4. rename the existing one

5. rename the new one to dict.sqlite

6. test it - it should work immediately after you restart firefox


Howto make your own
---------------------------------
I also included the script to modify the dictionary in place, but most of the time that'll be unnecessary to use.