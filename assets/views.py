from django.http import FileResponse

def asset(request, file_name: str):
    path = "assets/files/"

    if file_name.split('_')[-1] == 'css':
        path += 'css/'
    elif file_name.split('_')[-1] == 'jpg':
        path += 'images/'

    path += file_name.replace('_', '.')

    return FileResponse(open(path, "rb"))
