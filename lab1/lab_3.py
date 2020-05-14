
from gps import gps

problem = {

    'initial': ['Answer is Unknown', 'Internet is disconnected', 'Library is Closed'],
    'goal': ['Know Answer to Universe'],
    'actions': [
        {
            'action': 'Find Answer to Universe',
            'preconds': [
                'Internet is Connected',
                'I studied',
            ],
            'add': [
                'All I could find was 42',
            ],
            'delete': [
                'Internet is Connected',
                'I studied'
            ]
        },
        {
            'action': 'Turn Internet On',
            'preconds': [
                'Internet is disconnected',
            ],
            'add': [
                'Internet is Connected',
            ],
            'delete': [
                'Internet is disconnected',
            ]
        },
        {
            'action': 'Break Into Library and Study',
            'preconds': [
                'Library is Closed',
            ],
            'add': [
                'I studied',
            ],
            'delete': [
                'Library is Closed',
            ]
        },
    ]
}

if __name__ == '__main__':

    # Use GPS to solve the problem formulated above.
    actionSequence = gps(
        problem['initial'],
        problem['goal'],
        problem['actions']
    )

    # Print the solution, if there is one.
    if actionSequence is not None:
        for action in actionSequence:
            print(action)
    else:
        print('plan failure...')
