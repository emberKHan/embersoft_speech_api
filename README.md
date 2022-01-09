# EMBERSOFT_SPEECH_API_LITE
## Speech API for ARD speech commands.

## Overview

The server receives audio file, and returns the resulting text in a json dict.

## Requirements

**python3**
**hamachi** (for beta)
**haguichi** (if using linux based system, useful as a GUI frontend for hamachi)

Python packages:

**requests**

## Pre-requisites

0. Install Python3 and python-pip
1. Install [hamachi](https://vpn.net/) and [haguichi](https://haguichi.net/)

## Usage

Currently, the server is running on one of our machines. To get access, join the following hamachi network:

`network id: embersoft-steppe-01
password: thereissomethingaboutus`

This step will be unnecessary in the near future, once we deploy the model on a public server.

Provided [sender.py](https://github.com/emberKHan/embersoft_speech_api/blob/main/sender.py) as an example of sending a request. The script sends an audio file and returns speech to text results as json with the key *text*. Default mode is *force*, which forces the text results to pre-given text (in this case, the bigrams from the list of ARD commands). 

### Command line usage:

`python sender.py <path/to/audiofile>`

To get raw outputs:
`python sender.py <path/to/audiofile> --mode raw`

Example response:
    `{'text': 'ард койн утасны дугаараар шилжүүлэг хийх'}`
