#!/usr/bin/env python3
#
# Copyright this project and it's contributors
# SPDX-License-Identifier: Apache-2.0
#
# encoding=utf8

from __future__ import print_function
import os.path
import requests

# The ID of a sample document.
documents = [
        {'id': '1c_cUR1wWgAFlckHFAbKCl0lQ5Bt9d_X54rkfTRDqvyA','mimeType':'application/pdf','filename':'LF Energy High Level Overview Deck.pdf'},
        {'id': '1c_cUR1wWgAFlckHFAbKCl0lQ5Bt9d_X54rkfTRDqvyA','mimeType':'application/vnd.openxmlformats-officedocument.presentationml.presentation','filename':'LF Energy High Level Overview Deck.pptx'},
        {'id':'1scoG9tuWM3mSRFTFgw5ObVFF6L06nYfztE2gKaFs1_8','mimeType':'application/pdf','filename':'LF Energy Membership Overview.pdf'},
        ]


# Retrieve the documents contents from the Docs service.
for document in documents:
    print("Getting file {}...".format(document['filename']))
    try:
        match document['mimeType']:
            case 'application/pdf':
                exportFormat = 'pdf'
            case 'application/vnd.openxmlformats-officedocument.presentationml.presentation':
                exportFormat = 'pptx'
            case _:
                continue
        contents = requests.get('https://docs.google.com/feeds/download/presentations/Export?id={docid}&exportFormat={exportFormat}'.format(docid=document['id'],exportFormat=exportFormat),stream=False)
        with open(document['filename'], 'wb') as f:
            f.write(contents.content)
    except HttpError as err:
        print(err.content)
