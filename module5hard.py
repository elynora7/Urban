import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __repr__(self):
        return f'{self.nickname}'


class Video:
    time_now = 0

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title}'


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                break

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        if user not in self:
            self.users.append(user)
            self.log_in(nickname, password)
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for arg in args:
            if arg not in self:
                self.videos.append(arg)

    def get_videos(self, search_string):
        results = []
        for video in self.videos:
            if search_string.lower() in video.title.lower():
                results.append(video)
        return results

    def watch_video(self, name):
        if self.current_user:
            for video in self.videos:
                if video.title == name:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        break
                    else:
                        while video.time_now < video.duration:
                            video.time_now += 1
                            print(f'{video.time_now}', end=' ')
                            time.sleep(1)

                        print('Конец видео')
                        video.time_now = 0
                    break
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def __contains__(self, item):
        if isinstance(item, Video):
            return any(item.title == obj.title for obj in self.videos)
        if isinstance(item, User):
            return any(item.nickname == obj.nickname for obj in self.users)
        return False


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
