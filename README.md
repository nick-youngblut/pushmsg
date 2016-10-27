[![Build Status](https://travis-ci.org/nick-youngblut/pushmsg.svg?branch=master)](https://travis-ci.org/nick-youngblut/pushmsg)

pushmsg
========

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



## Installation and updating

[[top](#sections)]

The pushbullet line magic can be installed from GitHub by executing:

```bash
pip install -e git+https://github.com/nick-youngblut/pushmsg#egg=pushmsg
```

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


## Changelog

[[top](#sections)]
