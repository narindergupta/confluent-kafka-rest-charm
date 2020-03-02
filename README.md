# Confluent-kafka-rest-charm

This charm will deploy confulent Kafka Rest Proxy from deb package.

# Building

    cd src/
    charm build

Will build the Kafka charm, and then the charm in `/tmp/charm-builds`.

# Operating

This charm uses the repository from confulent. It relates to zookeeper and
certificate authority.

    juju deploy /tmp/charm-builds/confluent-kafka-rest
    juju deploy zookeeper
    juju deploy easyrsa
    juju relate confluent-kafka-rest zookeeper
    juju relate confluent-kafka-rest easyrsa

# Notes

The confulent Kafka Rest Proxy charm requires at least 4GB of memory.

# Details

Much of the charm implementation is borrowed from the Apache kafka
charm, but it's been heavily simplified and pared down. Jinja templating is
used instead of Puppet, and a few helper functions that were imported from
libraries are inlined.

---
