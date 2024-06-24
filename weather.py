from requests_html import HTMLSession

def Weather():
    try:
        s = HTMLSession()
        query = "karachi"
        url = f'https://www.google.com/search?q=weather+{query}'
        r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'})

        temp_element = r.html.find('span#wob_tm', first=True)
        unit_element = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True)
        desc_element = r.html.find('span#wob_dc', first=True)

        if temp_element and unit_element and desc_element:
            temp = temp_element.text
            unit = unit_element.text
            desc = desc_element.text
            return f"{temp} {unit} {desc}"
        else:
            return "Weather information not found"
    except Exception as e:
        return f"Error fetching weather information: {str(e)}"

