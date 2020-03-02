#!/bin/bash

set -eu

export PATH=/usr/lib/jvm/default-java/bin:$PATH

if [ -e "/etc/kafka-rest/broker.env" ]; then
    . /etc/kafka-rest/broker.env
fi

/usr/bin/kafka-rest-start /etc/kafka-rest/kafka-rest.properties
