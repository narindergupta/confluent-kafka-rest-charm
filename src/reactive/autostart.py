from charms.layer.confluent_kafka_rest import confluent_kafka_rest

from charmhelpers.core import hookenv

from charms.reactive import when


@when('confluent_kafka_rest.started', 'zookeeper.ready')
def autostart_service():
    '''
    Attempt to restart the service if it is not running.
    '''
    kafkarest = confluent_kafka_rest()

    if kafkarest.is_running():
        hookenv.status_set('active', 'ready')
        return

    for i in range(3):
        hookenv.status_set(
            'maintenance',
            'attempting to restart confluent_kafka_rest, '
            'attempt: {}'.format(i+1)
        )
        kafkarest.restart()
        if kafkarest.is_running():
            hookenv.status_set('active', 'ready')
            return

    hookenv.status_set('blocked',
            'failed to start confluent_kafka_rest; check syslog')
