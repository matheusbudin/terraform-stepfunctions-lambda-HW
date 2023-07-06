# '''
# This is a super simple function. In the function, 
# we are logging the event object and context object 
# and set value as the value of the key key in the event object. 
# Finally, we are returning the updated event object.

# '''

import logging

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

def handler(event, context):
    LOGGER.info(f'Event Object: {event}')
    LOGGER.info(f'Context Object: {context}')
    event['key'] = 'value'
    return event
