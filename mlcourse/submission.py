def create_submission(ex_num):
    """
    Returns a function to help submit exercise exercise_number.
    """

    return lambda e, t: \
            '{} successfully submitted {}'.format(e, ex_num)
