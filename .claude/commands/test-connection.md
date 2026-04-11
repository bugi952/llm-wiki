---
description: "외부 API 연결 테스트. Phase 시작 전 또는 장애 시 실행"
allowed-tools: Bash(curl*), Bash(python*), Read
---

외부 서비스 연결 상태를 하나씩 확인한다.

## 1. Claude API
```bash
python -c "
from anthropic import Anthropic
client = Anthropic()
r = client.messages.create(model='claude-haiku-4-5-20251001', max_tokens=10, messages=[{'role':'user','content':'ping'}])
print('Claude API: OK -', r.content[0].text)
"
```

## 2. Telegram Bot
```bash
python -c "
import os, requests
token = os.environ['TELEGRAM_BOT_TOKEN']
r = requests.get(f'https://api.telegram.org/bot{token}/getMe')
print('Telegram:', 'OK' if r.ok else 'FAIL', r.json().get('result',{}).get('username',''))
"
```

## 3. FRED API
```bash
python -c "
import os, requests
key = os.environ['FRED_API_KEY']
r = requests.get(f'https://api.stlouisfed.org/fred/series?series_id=GDP&api_key={key}&file_type=json')
print('FRED:', 'OK' if r.ok else 'FAIL')
"
```

## 4. 한국은행 ECOS API
```bash
python -c "
import os, requests
key = os.environ['ECOS_API_KEY']
r = requests.get(f'https://ecos.bok.or.kr/api/StatisticSearch/{key}/json/kr/1/1/722Y001/M/202401/202401')
print('ECOS:', 'OK' if r.ok else 'FAIL')
"
```

## 5. Finnhub API
```bash
python -c "
import os, requests
key = os.environ['FINNHUB_API_KEY']
r = requests.get(f'https://finnhub.io/api/v1/calendar/economic?token={key}')
print('Finnhub:', 'OK' if r.ok else 'FAIL')
"
```

## 6. GitHub Push (vault 레포)
```bash
cd vault && git remote -v && git fetch --dry-run 2>&1 && echo 'GitHub: OK' || echo 'GitHub: FAIL'
```

## 7. RSSHub (셀프호스팅)
```bash
curl -s -o /dev/null -w '%{http_code}' http://localhost:1200/ | grep -q 200 && echo 'RSSHub: OK' || echo 'RSSHub: FAIL (not running?)'
```

## 8. arXiv RSS
```bash
curl -s -o /dev/null -w '%{http_code}' 'https://rss.arxiv.org/rss/cs.AI' | grep -q 200 && echo 'arXiv RSS: OK' || echo 'arXiv RSS: FAIL'
```

## 리포트

```
## Connection Test
- Claude API:  OK / FAIL
- Telegram:    OK / FAIL
- FRED:        OK / FAIL
- ECOS:        OK / FAIL
- Finnhub:     OK / FAIL
- GitHub:      OK / FAIL
- RSSHub:      OK / FAIL (Phase 2)
- arXiv RSS:   OK / FAIL

Overall: N/8 connected
```

Phase 1은 Claude API + GitHub + arXiv RSS가 필수. 나머지는 Phase 2+.
