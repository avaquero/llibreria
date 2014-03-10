def social_details(strategy, response, *args, **kwargs):
    import md5
    details = strategy.backend.get_user_details(response)
    email = details['email']
    fakemail = unicode( md5.new(email).hexdigest() )
    new_details = {
                'username': fakemail[:5],
                'email': fakemail + '@noreply.com',
                'fullname': fakemail[:5],
                'first_name': details['first_name'],
                'last_name': '' }
    return {'details': new_details }