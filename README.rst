Suzune
======

Suzune is a command line image registration tool.

Why Suzune
----------

When I chat with my friend or write a comment to some issues,
sometime I want to paste a image which is corresponding to the situation.

similar web service is like `LGTM.in <http://lgtm.in/>`_
or `GIFGIF <http://gifgif.media.mit.edu/>`_

How to install
--------------

Install suzune from github. Now this package is not uploaded to PyPI::

    $ pip install git+https://github.com/hirokiky/suzune.git

How to use
----------

If you want to get an 'smile' image, pass the word as first argument::

    $ suzune get smile

Then suzune will search a smiling image from it's database
and show up a image selected in random on your browser.

Maybe you wonder that what kind of tags you can get.
To answer, suzune has 'tags' sub command which will display all of tags in it's database::

    $ suzune tags
    angry (2)
    cat (5)
    cute (4)
    lgtm (3)
    thumbup (8)

Not only getting images, suzune also provides 'add' command to register your favorite images
into suzune's database.

    $ suzune add http://image.example.com/an_angry_cat.jpg angry cat cute

Notice that the database is placed on your local environment.

Where to store
--------------

Stored data will place on '~/.suzune/db.json'.
If you want to reset the database or remove Suzune it's own, Just remove this directory.

What Suzune mean?
-----------------

Suzune is a anime character appearing in Love-lab.

http://www.love-lab.tv/chara/suzu.html
