import gevent
from gevent import monkey
monkey.patch_all()
from bottle import route, run, template, get, post, static_file, request, redirect, auth_basic

is_the_server_started = True

@post('/start')
def start():
    global is_the_server_started
    if not is_the_server_started:
        is_the_server_started = True
    return

@get('/')
def endpoint1():
    if not is_the_server_started:
        return 'Please start the server'
    list_of_interfaces = ['/happy', '/notsohappy']
    return {'My interfaces are: ': list_of_interfaces}

@get('/happy')
def endpoint2():
    if not is_the_server_started:
        return 'Please start the server'
    req_string = request.GET.get('name', '').strip()
    return {
        'response' : 'What a fine day today? ' + req_string,
        'date' : '23/9/2016'
    }


valid_users = {'ashwin' : '100',
                'rags' : '101'
               }

def auth_func(username, password):
    if username in valid_users:
        if password == valid_users[username]:
            return True
    return False
        

@get('/notsohappy')
@auth_basic(auth_func)
def endpoint3():
    if not is_the_server_started:
        return 'Please start the server'

    req_string = request.GET.get('name', '').strip()
    return {'response' : 'Todays traffic is so crappy? ' + req_string}

if __name__ == '__main__':
    run(host='0.0.0.0', port=9007, server='gevent')


