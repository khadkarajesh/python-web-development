class User:
    def __init__(self, *args, **kwargs):
        self.id = args[0]
        self.age = args[1]
        self.name = kwargs['name']
        self.profession = kwargs['profession']

        print(args, kwargs)
        print(F'id={self.id} '
              F'age={self.age}'
              F'name={self.name}'
              F'profession={self.profession}')


if __name__ == '__main__':
    user = User(1, 50, name='Bob Marley', profession='Singer')
    print(user)
