import re
import time
import system_book_timer
import system_config
import system_function

import huel_library_urls

if __name__ == "__main__":

    print("准备进入系统......")
    response = system_function.into_index(huel_library_urls.index_url)
    if "来选座" in response:
        print("成功进入系统......")
    result = system_function.obtain_js(response)
    request_js = result[1]
    need_js = re.findall(r"layout/(.+?).js",request_js)
    print("验证码已获取："+need_js[0])
    verify_code = system_config.js_code.get(need_js[0])
    url = huel_library_urls.booked_url+verify_code+'=12,14&yzm='
    print("选座已就绪......")
    while system_book_timer.timer_setting():
        while True:
            result = system_function.booking(url)
            print(result)
            if '成功' in result:
                print("选座成功")
                break
            print("重试...")
            time.sleep(0.1)

