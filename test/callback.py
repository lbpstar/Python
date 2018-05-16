def do(a):
    print('do', a)
    CallBackMgr.callback(5, lambda a = a: post_do(a))
 
def post_do(a):
    print('post_do', a)
do(8)