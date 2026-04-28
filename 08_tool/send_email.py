
# 授权码获取路径：163 企业邮 → 设置 → 客户端设置 → 生成客户端授权密码。
# USER = "xxx@163.com" 发送者
# p.add_argument("--to", default="xxx@other.com") 接受者
# python3 send_email.py --subject "标题" --body "内容" 


import smtplib, ssl, argparse, os
from email.mime.text import MIMEText
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
print('env_path', env_path)
load_dotenv()
USER = os.environ["EMAIL_USER"]
PASSWORD = os.environ["EMAIL_PASSWORD"]

p = argparse.ArgumentParser()
# p.add_argument("--to", default="xxx@other.com")
p.add_argument("--subject", required=True)
p.add_argument("--body", required=True)
# p.add_argument("--password", required=True)
a = p.parse_args()


msg = MIMEText(a.body, "plain", "utf-8")
# msg["From"], msg["To"], msg["Subject"] = USER, a.to, a.subject
msg["From"], msg["Subject"] = USER, a.subject

with smtplib.SMTP_SSL("smtp.qiye.163.com", 465, context=ssl.create_default_context()) as s:
    s.login(USER, PASSWORD)
    # s.sendmail(USER, [a.to], msg.as_string())
    s.sendmail(USER, [USER], msg.as_string())

# print(f"✅ 已发送: {a.subject} → {a.to}")
print(f"✅ 已发送: {a.subject} → {USER}")
