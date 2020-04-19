class User:
    def __init__(self, name, engagement):
        self.name = name
        self.engagement_metrics = engagement
        self.score = 0

    def __repr__(self):
        return f'<User {self.name}>'


def get_user_score(user):
    try:
        return perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function.')


def email_engaged_user(user):
    try:
        user.score = perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function.')
        raise
    else:
        if user.score > 500:
            send_engagement_notification(user)


def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2


def send_engagement_notification(user):
    print(f'Notification sent to {user}.')


# my_user = User('Rolf', {'clicks': 61, 'hits': 100})
# email_engaged_user(my_user)


def interact():
    while True:  # keep looping until user reach break statement
        try:
            user_input = int(input('Please input an integer:'))  # turn the user input into an integer
            # print out the message '{user_input} is {even/odd}.'
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))
        except ValueError:
            print("Please input integers only.")
        finally:
            user_input = input('Do you want to play again? (y/N):')
            if user_input != 'y':  # quit if the user didn't input `y`
                print('Goodbye.')
                break  # break the while loop to quit

interact()