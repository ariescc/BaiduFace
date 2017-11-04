from aip import AipFace

APP_ID = '10317971'
API_KEY = 'IMWQoDHYUxNOqLg4uOUPHEwC'
SECRET_KEY = 'dorWf1FcRR4fqh0XBqKCzoFbP6cYQgiq'

aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(path):
    with open(path, 'rb') as fp:
        return fp.read()


def face_detect(path):
    options = {
        'max_face_num': 10,
        'face_fields': "age, beauty, expression, faceshape",
    }
    result = aipFace.detect(path, options)
    return result


def face_match(images):
    options = {
        'result': "score",
    }
    result = aipFace.match(images, options)
    return result

if __name__ == '__main__':
    image1 = get_file_content('erren.jpg')
    # image2 = get_file_content('b.jpg')
    # images = [image1, image2]

    c1 = get_file_content('fa.jpg')
    c2 = get_file_content('c.jpg')
    lan = get_file_content('lanni.jpg')
    images = [c1, c2]

    # print face_match(images)
    print face_detect(lan)
