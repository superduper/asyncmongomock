.. container::

   .. image:: http://vmalloc.github.io/mongomock/mongomock-small.png


What is this?
-------------

Asyncmongo compatible ``mongomock`` implementation


Important Note About Project Status & Development
-------------------------------------------------

MongoDB is complex. This library aims at a reasonably complete mock of MongoDB for testing purposes, not a perfect replica. This means some features are not likely to make it in any time soon.

Also, since many corner cases are encountered along the way, our goal is to try and TDD our way into completeness. This means that every time we encounter a missing or broken (incompatible) feature, we write a test for it and fix it. There are probably lots of such issues hiding around lurking, so feel free to open issues and/or pull requests and help the project out!

**NOTE**: We don't include pymongo functionality as "stubs" or "placeholders". Since this library is used to validate production code, it is unacceptable to behave differently than the real pymongo implementation. In such cases it is better to throw `NotImplementedError` than implement a modified version of the original behavior.

Acknowledgements
----------------

Many thanks go to the following people for helping out:

* Alec Perkins
* Austin W Ellis
* Andrey Ovchinnikov
* Arthur Hirata
* Corey Downing
* Craig Hobbs
* David Fischer
* Edward D'Souza
* Eugene Chernyshov
* Israel Teixeira
* Jacob Perkins
* Jason Sommer
* Jeff McGee
* Joël Franusic
* Mike Ho
* Nigel Choi
* Omer Gertel
* Scott Sexton
* Todd Tomkinson 
* catty (ca77y _at_ live.com)
* emosenkis
* waskew (waskew _at_ narrativescience.com)
* zcarter
