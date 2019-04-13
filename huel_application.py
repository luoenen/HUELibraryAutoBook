import re
import system_config
import system_function
import system_book_timer
import huel_library_urls

if __name__ == "__main__":

    response = system_function.into_index(huel_library_urls.index_url)
    result = system_function.obtain_js(response)
    request_js = result[1]
    need_js = re.findall(r"layout/(.+?).js",request_js)
    verify_code = system_config.js_code.get(need_js[0])
    url = huel_library_urls.booking_url+''+verify_code+''
    while system_book_timer:
        result = system_function.booking(url)
        if '成功' in result:
            break
        else:
            print("选座失败，开始重选")

