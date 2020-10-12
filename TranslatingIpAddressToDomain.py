import asyncio


def qwe(tagets: list):
    '''
    :param tagets:
    :return: urlss
    '''

    async def main(loop, targets):
        '''
        :param loop:
        :param targets:
        :return: urls
        '''
        urls = []
        for target in targets:
            info = await loop.getnameinfo(target)
            print(info[0])
            u = info[0].split('.')
            if not u[0].isdigit():
                h = info[0].split('.')[-2:]
                if f'{h[0]}.{h[1]}' not in urls:
                    urls.append(f'{h[0]}.{h[1]}')
        print(urls)

        return urls

    event_loop = asyncio.get_event_loop()
    try:
        urlss = event_loop.run_until_complete(main(event_loop, tagets))
        return urlss
    except:
        print('ошибка получения url')
