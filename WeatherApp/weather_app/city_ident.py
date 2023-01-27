def city_ident(request):
    city = ''
    request = str(request)
    if 'city=' in request:
        tmp_request = request
        tmp_request = tmp_request[26:]
        index = 0
        while tmp_request[index] != '&':
            city += tmp_request[index]
            index += 1

    return city
