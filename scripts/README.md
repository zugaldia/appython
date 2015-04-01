# Appython scripts

This folder contains three scripts:

* `prepare_build.py` is used by the `Makefile` rules in the `samples` folder to increment the build number, and set the right stage, before running the app locally, or deploying it to production. You normally won't need to run this directly, as the `Makefile` will take care of it.

You can test it, for example, with:

```
$ python prepare_build.py --filename=prepare_build_test.txt
```

* `generate.py` uses the `appython` library to generate a bunch of random strings. In particular, the result of `generate_secret()` (called `key` in the output) is useful to set up the `SECRET_KEY` of the Flask app.

You can run it with:

```
$ python generate.py
```

* `ln_plus.py` helps the `Makefile` create symlinks. See the comment at the beginning of the file for more information and an example.
