# City Wharf 永久微信群活码（GitHub Pages 版）

这个项目采用“固定入口二维码 + 可替换群二维码图片”的方式：

- 海报上的永久二维码指向你的 GitHub Pages 网页。
- 网页显示 `assets/group-qr.png`。
- 每次微信群二维码到期时，只需用新图片覆盖这个文件，并更新 `config.js` 中的日期，再提交到 GitHub。
- 海报上的永久二维码不需要重新生成。

> 重要：这不会把微信官方的 7 天群二维码变成永久二维码。它只是让外层网页地址保持不变。访客扫描后会打开网页，再按页面提示使用当前群二维码加入群聊。

## 一、准备文件

1. 解压 ZIP。
2. 用微信生成一张当前有效的微信群二维码。
3. 将图片命名为 **`group-qr.png`**，放进 `assets` 文件夹，覆盖同名文件。
4. 建议使用微信原始二维码图片，不要用 AI 重绘或加装饰，以免影响识别。

## 二、创建 GitHub 仓库

1. 登录 https://github.com/ 并注册/登录账号。
2. 点击右上角 `+` → `New repository`。
3. Repository name 填：`city-wharf-wechat-qr`（也可以自定义）。
4. 选择 **Public**。GitHub Free 通常要求公开仓库才能使用 Pages。
5. 点击 `Create repository`。
6. 把本项目文件和 `assets/group-qr.png` 上传到仓库根目录（不要只上传 ZIP；需要先解压）。
7. 点击 `Commit changes` 保存。

## 三、开启 GitHub Pages

1. 打开仓库的 `Settings`。
2. 左侧找到 `Pages`。
3. 在 `Build and deployment` → `Source` 选择 `Deploy from a branch`。
4. Branch 选择 `main`，文件夹选择 `/(root)`。
5. 点击 `Save`。
6. 等待部署完成。回到 `Settings` → `Pages`，页面会显示网址，通常类似：

   `https://你的GitHub用户名.github.io/city-wharf-wechat-qr/`

请用手机打开这个网址，确认网页能显示最新群二维码。

## 四、生成印在海报上的永久二维码

注意：要编码的是上一步 GitHub Pages 显示的完整网址，而不是微信群的 7 天二维码。

### 方法 A：用 Python 生成（推荐、无第三方水印）

在电脑终端进入解压后的项目文件夹，执行：

```bash
python3 -m pip install -r requirements.txt
python3 generate_qr.py "https://你的GitHub用户名.github.io/city-wharf-wechat-qr/"
```

生成的 `city-wharf-permanent-qr.png` 就是海报使用的固定二维码。请先用另一台手机测试扫描，确认能打开网页，再交付印刷。

如果电脑上 `python3` 不可用，也可以安装 Python 3 后再运行。脚本只在本地生成二维码，不会上传你的二维码或网址到第三方二维码网站。

## 五、每 7 天更新群二维码

1. 在微信里生成新的群二维码。
2. 下载/保存原始二维码图片。
3. 将它重命名为 `group-qr.png`。
4. 在 GitHub 仓库打开 `assets` 文件夹，上传新图片并覆盖旧文件。
5. 打开 `config.js`，把 `LAST_UPDATED` 改成当天日期，例如：

   ```js
   const LAST_UPDATED = "2026-11-11";
   ```

6. 点击 `Commit changes`。
7. 等待 GitHub Pages 更新，然后用手机打开网页检查新二维码。

**海报上的固定二维码不变**，只需要更新网页中的群二维码图片。

## 六、非常重要的限制和安全提醒

- GitHub Pages 是公开网站；仓库设为 Public 时，网页和群二维码图片任何人都可能访问。不要把它当作私密邀请链接。
- 任何拿到当前群二维码的人，都可能在二维码有效期内尝试加入群聊。请只在你愿意公开招募成员时使用。
- 群达到人数上限、群主关闭加入、微信风控或其他平台限制时，访客仍可能无法加入；这个网页无法绕过微信限制。
- 该项目不自动读取微信二维码有效期，也不会自动提醒你更新。建议你在手机日历中设置每 6 天提醒一次，留出更换时间。
- 网页显示的更新日期只是你手动填写的日期，不代表微信官方验证了二维码仍然有效。
- GitHub Pages 的部署和缓存更新可能需要几分钟。换图后如手机仍显示旧图，可稍后重试或刷新页面。

## 七、故障排查

**网页显示图片破损：**
- 检查图片路径是否严格为 `assets/group-qr.png`。
- 检查文件名大小写是否一致。
- 确认上传的是 PNG 图片。

**网页打不开：**
- 检查仓库是否 Public。
- 检查 Pages 是否选择 `main` 和 `/(root)`。
- 在仓库 `Actions` 中检查 Pages 部署是否成功。

**二维码扫不开：**
- 确认永久二维码编码的是完整 GitHub Pages URL，末尾建议保留 `/`。
- 不要把二维码压缩得太小；印刷前先用多台手机测试。
- 不要在二维码中心覆盖 Logo，也不要改变二维码黑白模块。
