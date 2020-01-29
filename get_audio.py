from vk_api.audio import VkAudio
import vk_api


def get(user_id=None, album_id=None):
    login, password = '+79534940476', 'kek1488kek'
    vk_session = vk_api.VkApi(login, password)

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    regulator = VkAudio(vk_session)
    audio_url = regulator.get(owner_id=user_id, album_id=album_id)
    f = open('audio.txt', 'a')
    for item in audio_url:
        audioWrite = 'audio' + str(user_id) + '_' + str(item['id']) + '\n'
        f.write(audioWrite)
    print('Запись успешно завершена')
    f.close()
