# 接口细节

四个接口按顺序调，顺序错了就是白跑。所有请求都要带 `access_token`。

## 0. 取 token

```
POST https://api.weixin.qq.com/cgi-bin/stable_token
{"grant_type":"client_credential","appid":"...","secret":"...","force_refresh":false}
→ {"access_token":"...","expires_in":7200}
```

老接口兜底：`GET /cgi-bin/token?grant_type=client_credential&appid=&secret=`。

有效期 7200 秒。脚本缓存在系统临时目录，提前 5 分钟刷新，文件权限 600。

## 1. 正文图片换图床

```
POST /cgi-bin/media/uploadimg?access_token=...
form-data: media=@local.jpg
→ {"url":"http://mmbiz.qpic.cn/mmbiz_jpg/xxxx/0"}
```

三条硬限制：

- 只收 jpg / png
- **单张必须小于 1MB**
- 不占素材库那 5000 张的配额

返回的 `url` 才是能写进正文的地址。外链、本地路径、第三方图床一律会被过滤，且微信有 Referer 防盗链。

## 2. 封面转永久素材

```
POST /cgi-bin/material/add_material?access_token=...&type=image
form-data: media=@cover.png
→ {"media_id":"...","url":"..."}
```

这个 `media_id` 就是 `thumb_media_id`。

**不能混用**：正文图走 `uploadimg`（拿 URL），封面走 `add_material`（拿 media_id）。用 `media/upload` 的临时素材当封面会得到 `40007`，因为临时素材 3 天过期，草稿接口拒收。

封面建议 2.35:1，900×383，小于 10MB。

## 3. 写草稿

```
POST /cgi-bin/draft/add?access_token=...
{"articles":[{
  "title":"...",
  "author":"...",
  "digest":"...",
  "content":"<section>...</section>",
  "thumb_media_id":"...",
  "need_open_comment":0,
  "only_fans_can_comment":0
}]}
→ {"media_id":"草稿id"}
```

要点：

- `content` 是 HTML 字符串，只支持微信白名单标签：`section` `p` `span` `strong` `em` `img` `ul` `ol` `li` `table` `br` `hr`
- 中文必须 `json.dumps(..., ensure_ascii=False).encode("utf-8")`，请求头带 `charset=utf-8`，否则进草稿箱是乱码
- 必须服务端调用，不能在前端/小程序里直接调

## 4. 发布（本 Skill 不调用）

```
POST /cgi-bin/freepublish/submit
```

2025 年 7 月起，个人主体、未认证企业号、不支持认证的账号已被回收该权限。只有认证的服务号/订阅号可用，且订阅号每天只能群发 1 次。

留着让用户自己点，是设计选择，不是能力不足。

## 错误码

| 码 | 含义 | 处置 |
|---|---|---|
| 40001 | token 失效 | 重新取（脚本自动） |
| 40007 | media_id 无效 | 封面必须走 `add_material` |
| 40008 | 消息长度超限 | 正文压缩到 20000 字内 |
| 40009 | 图片不合规 | 正文图转 jpg/png 并压到 1MB 内 |
| 40164 | IP 不在白名单 | 后台加公网 IP；NAT 环境 IP 会变 |
| 45004 | 摘要超长 | 128 字以内 |
| 45009 | 调用超频 | 稍等，别连发 |
| 48001 | 接口未授权 | 账号未认证，改走粘贴路线 |

## 凭据

`WECHAT_APPID` 和 `WECHAT_APPSECRET`，在公众号后台「设置与开发 → 基本配置」里拿。AppSecret 只展示一次，丢了只能重置。

脚本从环境变量或当前目录 `.env` 读，不会写进任何日志或输出。`.env` 已加进 `.gitignore`。
