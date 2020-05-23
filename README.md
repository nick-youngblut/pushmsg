![.github/workflows/pythonpackage.yml](https://github.com/nick-youngblut/pushmsg/workflows/.github/workflows/pythonpackage.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/pushmsg.svg)](http://badge.fury.io/py/pushmsg)

pushmsg
=======

An IPython magic extension for sending notifications with [Pushbullet](https://www.pushbullet.com/)

#### Sections

- [Examples](#examples)
- [Installation and updating](#installation-and-updating)
- [Usage](#usage)
- [Changelog](#changelog)


## Examples

### Send a notification (to computer, phone, tablet, etc)

`%pushmsg "my long job just finished"`

### Add a Pushbullet API key

`%pushmsg --add my_key=o.xhsySHlsuslUX`

### List Pushbullet API keys (multiple keys supported)

`%pushmsg --list`

### Wait for an SGE job to complete, then send a notification

`%pushmsg_qstat --job my_sge_job "my SGE job just finished"`

### Wait for all SGE jobs to complete, then send a notification

`%pushmsg_qstat "All SGE jobs are finished"`

### Send notifications from the command line

`pushmsg "Job finished"`


## Installation and updating

[[top](#sections)]

The pushbullet line magic can be installed with pip by executing:

```bash
pip install pushbullet.py pushmsg
```

The development version of pushmsg line magic can be installed from GitHub by executing:

```bash
pip install -e git+https://github.com/nick-youngblut/pushmsg#egg=pushmsg
```

> If using the dev version, make sure to install `pushbullet.py`

### Pushbullet API key

1. Sign up for a [Pushbullet account](https://www.pushbullet.com/).
1. Add some devices to your account (eg., computer, phone, tablet).
1. Get an API key ("Access Tolkens" under "Settings")
1. Add the API key to your .pushbullet config (see usage)

## Usage

[[top](#sections)]

After successful installation, the `pushmsg` magic extension can be loaded via:

`%load_ext pushmsg`

To get an overview of all available options, type:

`%pushmsg?`

To add an Pushbullet API key:

`%pushmsg -a my_key=o.FgVQMqK5IvASJOxllx`

To send a message:

`%pushmsg "my long job is complete!"`


### Sun Grid Engine jobs 

Wait for an SGE job to complete, then send a notification:

`%pushmsg_qstat --job my_sge_job "my SGE job just finished"`

Wait for all SGE jobs to complete, then send a notification:

`%pushmsg_qstat "All SGE jobs are finished"`


### Command line 

`pushmg "job complete"`

## Changelog

[[top](#sections)]

### v0.2.2 

* Added pushmsg command line script

### v0.2.0 

* Added %pushmsg_qstat line magic and documentation

