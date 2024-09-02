import platform
import speedtest

st = speedtest.Speedtest()
download_speed = st.download() / (1024 ** 2)
upload_speed = st.upload() / (1024 ** 2)

print(f'Тип системы: {platform.platform()}',
      f'Установленный процессор: {platform.processor()}',
      f'Текущая версия компилятора: {platform.python_compiler()}',
      f'Текущая версия python: {platform.python_version()}', sep='\n')

print(f'\nСкорость загрузки: {download_speed:.2f}',
      f'Скорость отдачи: {upload_speed:.2f}', sep='\n')
