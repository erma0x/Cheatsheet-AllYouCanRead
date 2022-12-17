from tqdm import tqdm
from time import sleep

def progression_bar_linear():


    for i in tqdm(range(100)):
        sleep(0.02)
progression_bar_linear()

def progression_bar_hashtag():
    from time import sleep
    from progress.bar import Bar

    with Bar('Processing Evolution...') as bar:
        for i in range(100):
            sleep(0.01)
            bar.next()

progression_bar_hashtag()
