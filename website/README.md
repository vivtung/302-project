## Setup Instructions

#### For debian based distubutions:

    sudo apt-get install python-dev python-pip
    sudo pip install virtualenv
    virtualenv --no-site-packages ~/venv
    source ~/venv/bin/activate

Now we need to setup the database:

    sudo apt-get install postgresql libpq-dev
    # run the sql scripts and stuff..

Finally, `cd` into the `website` directory and then run:
`pip install -r requirements.txt` to install the dependencies required for the
application and `python run.py` to start the web server.
