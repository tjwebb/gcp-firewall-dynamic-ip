def checkip(request):
    return (request.headers['x-forwarded-for'], 200, { })
