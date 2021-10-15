# copyright ©️ 2021 rizad
# !/usr/bin/python
import os
import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from PIL import Image
import shutil
from time import sleep
import fitz
import convertapi

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN, parse_mode="Markdown")

if os.getenv("CONVERT_API") is not None:
    convertapi.api_secret = os.getenv("CONVERT_API")


@bot.message_handler(commands=["start"])
def strt(message):
    
    try:
        bot.send_chat_action(message.chat.id, "typing")
        strtMsg = f"""
Hey [{message.from_user.first_name}](tg://user?id={message.chat.id})..!! This bot will helps you to converts image To pdf & vice-versa

Some of the main features are:
◍ `Convert images to PDF`
◍ `Convert PDF to images`
◍ `Convert files to pdf`
"""
        key = types.InlineKeyboardMarkup()
        key.add(
            types.InlineKeyboardButton("About", callback_data="strtDevEdt"),
            types.InlineKeyboardButton('Developer', url='https://telegram.me/rizad_x96'),
        )
        bot.send_message(
            message.chat.id, strtMsg, disable_web_page_preview=True, reply_markup=key
        )

        @bot.callback_query_handler(func=lambda call: call.data)
        def strtMsgEdt(call):
            edit = call.data

            if edit == "strtDevEdt":

                try:
                    aboutDev = """
ʜᴇʏ ɪᴀᴍ ᴘᴅғ ɪᴅᴇ..
sᴇɴᴅ ᴍᴇ ᴛʜᴇ ғɪʟᴇs ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴄᴀɴ..

➪ Project Name : ᴘᴅғ ɪᴅᴇ
➪ Author : [rizadッ](https://telegram.me/rizad_x96)
➪ Library : Pyrogram
➪ Language : Python
➪ License Type : GNU General public License (GPL)"""
                    key = types.InlineKeyboardMarkup()
                    key.add(
                        types.InlineKeyboardButton("Home", callback_data="back"),
                        types.InlineKeyboardButton("More", callback_data="imgsToPdfEdit"),
                    )
                    bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text=aboutDev,
                        disable_web_page_preview=True,
                        reply_markup=key,
                    )
                
                except Exception:
                    pass
            
            elif edit == "imgsToPdfEdit":
            
                try:
                    expMsg = """
Images to pdf :

  Just Send me some images & use /generate to get your pdf..

 ◍ Image Sequence will be considered
 ◍ For better quality pdfs(send images without Compression) 
 ◍ `/cancel` - Delete's the current Queue
 ◍ `/id` - to get your telegram ID 
 ◍ RENAME YOUR PDF:
 
  - By default, your telegram ID will be treated as your pdf name..🙂
  - `/generate fileName` - to change pdf name to fileName🤞
  - `/generate name` - to get pdf with your telegram name

[Developer](https://telegram.me/rizad_x96)"""
                    key = types.InlineKeyboardMarkup()
                    key.add(
                        types.InlineKeyboardButton("Home", callback_data="back"),
                        types.InlineKeyboardButton(
                            "PDF to images", callback_data="pdfToImgsEdit"
                        ),
                    )
                    bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text=expMsg,
                        disable_web_page_preview=True,
                        reply_markup=key,
                    )
                
                except Exception:
                    pass
            
            elif edit == "pdfToImgsEdit":
                
                try:
                    expMsg = """
PDF to images:

 Just Send me a pdf file.

 ◍ I will Convert it to images
 ◍ if Multiple pages in pdf(send as albums) 
 ◍ Page numbers are sequentially ordered 
 ◍ Send images faster than anyother bots 
 
[Developer](https://telegram.me/rizad_x96)"""
                    key = types.InlineKeyboardMarkup()
                    key.add(
                        types.InlineKeyboardButton(
                            "Imgs To Pdf", callback_data="imgsToPdfEdit"
                        ),
                        types.InlineKeyboardButton("Home", callback_data="back"),
                        types.InlineKeyboardButton(
                            "file to Pdf", callback_data="filsToPdfEdit"
                        ),
                    )
                    bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text=expMsg,
                        disable_web_page_preview=True,
                        reply_markup=key,
                    )
                
                except Exception:
                    pass
            
            elif edit == "filsToPdfEdit":
            
                try:
                    expMsg = """
Files to PDF:

Just Send me a Supported file.. I will convert it to pdf.

◍ Supported files(.epub, .xps, .oxps, .cbz, .fb2)
◍ Only Images & ASCII characters Supported 
◍ added 30+ new file formats that can be converted to pdf.

[Developer](https://telegram.me/rizad_x96)"""
                    key = types.InlineKeyboardMarkup()
                    key.add(
                        types.InlineKeyboardButton(
                            "PDF to imgs", callback_data="imgsToPdfEdit"
                        ),
                        types.InlineKeyboardButton("Home", callback_data="back"),
                    )
                    bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text=expMsg,
                        disable_web_page_preview=True,
                        reply_markup=key,
                    )
                
                except Exception:
                    pass
            
            elif edit == "warningEdit":
            
                try:
                    expMsg = """
[Developer](https://telegram.me/rizad_x96)
"""
                    key = types.InlineKeyboardMarkup()
                    key.add(
                       types.InlineKeyboardButton("Home", callback_data="back"),
                    )
                    bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text=expMsg,
                        disable_web_page_preview=True,
                        reply_markup=key,
                    )
                
                except Exception:
                    pass
            
            elif edit == "back":
            
                try:
                    strtMsg = """
ʜᴇʏ ɪᴀᴍ ᴘᴅғ ɪᴅᴇ..
sᴇɴᴅ ᴍᴇ ᴛʜᴇ ғɪʟᴇs ᴡʜɪᴄʜ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴄᴀɴ..

➪ Project Name : ᴘᴅғ ɪᴅᴇ
➪ Author : [rizadッ](https://telegram.me/rizad_x96)
➪ Library : Pyrogram
➪ Language : Python
➪ License Type : GNU General public License (GPL)
"""
                    key = types.InlineKeyboardMarkup()
                    key.add(
                        types.InlineKeyboardButton(
                            "About", callback_data="strtDevEdt"
                        ),
                        types.InlineKeyboardButton(
                            "More 🥳", callback_data="imgsToPdfEdit"
                        ),
                    )
                    bot.edit_message_text(
                        chat_id=call.message.chat.id,
                        message_id=call.message.message_id,
                        text=strtMsg,
                        disable_web_page_preview=True,
                        reply_markup=key,
                    )
                
                except Exception:
                    pass
            
    except Exception:
        pass


@bot.message_handler(commands=["id"])
def UsrId(message):
    
    try:
        bot.send_chat_action(message.chat.id, "typing")
        bot.send_message(message.chat.id, f"Your ID - `{message.chat.id}`")
    
    except Exception:
        pass


@bot.message_handler(commands=["feedback"])
def feedback(message):
    bot.send_chat_action(message.chat.id, "typing")
    feedbackMsg = f"""
[Feedback](https://telegram.me/rizad_x96)
"""
    bot.send_message(message.chat.id, feedbackMsg, disable_web_page_preview=True)


PDF = {}
media = {}

@bot.message_handler(content_types=["photo"])
def pic(message):
    
    try:
        bot.send_chat_action(message.chat.id, "typing")
        picMsgId = bot.reply_to(
            message,
            "`Downloading your Image..`",
        )
        
        if not isinstance(PDF.get(message.chat.id), list):
            PDF[message.chat.id] = []
        
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        try:
            os.makedirs(f"./{message.chat.id}/imgs")
        
        except Exception:
            pass
        
        with open(f"./{message.chat.id}/imgs/{message.chat.id}.jpg", "wb") as new_file:
            new_file.write(downloaded_file)
        
        img = Image.open(
            f"./{message.chat.id}/imgs/{message.chat.id}.jpg"
        ).convert("RGB")
        
        PDF[message.chat.id].append(img)
        bot.edit_message_text(
            chat_id=message.chat.id,
            text=f"""`Added {len(PDF[message.chat.id])} page/'s to your pdf..`

/generate to generate PDF""",
            message_id=picMsgId.message_id,
        )
    
    except Exception:
        pass


@bot.message_handler(content_types=["document"])
def fls(message):
    
    try:
        bot.send_chat_action(message.chat.id, "typing")
        isPdfOrImg = message.document.file_name
        fileSize = message.document.file_size
        
        fileNm, fileExt = os.path.splitext(isPdfOrImg)
        suprtedFile = [".jpg", ".jpeg", ".png"]
        suprtedPdfFile = [".epub", ".xps", ".oxps", ".cbz", ".fb2"]
        suprtedPdfFile2 = [
            ".csv",
            ".doc",
            ".docx",
            ".dot",
            ".dotx",
            ".log",
            ".mpp",
            ".mpt",
            ".odt",
            ".pot",
            ".potx",
            ".pps",
            ".ppsx",
            ".ppt",
            ".pptx",
            ".pub",
            ".rtf",
            ".txt",
            ".vdx",
            ".vsd",
            ".vsdx",
            ".vst",
            ".vstx",
            ".wpd",
            ".wps",
            ".wri",
            ".xls",
            ".xlsb",
            ".xlsx",
            ".xlt",
            ".xltx",
            ".xml",
        ]
        
        if fileSize >= 10000000:
            
            try:
                bot.send_chat_action(message.chat.id, "typing")
                unSuprtd = bot.send_message(
                    message.chat.id,
                    """
Due to Overload, bot supports only 10mb files

`please Send me a file less than 10mb Size`
""",
                )
                sleep(15)
                bot.delete_message(
                    chat_id=message.chat.id, message_id=message.message_id
                )
                bot.delete_message(
                    chat_id=message.chat.id, message_id=unSuprtd.message_id
                )
            except Exception:
                pass
        
        elif fileExt in suprtedFile:
            
            try:
                picMsgId = bot.reply_to(
                    message,
                    "`Downloading your Image..`",
                )
                
                if not isinstance(PDF.get(message.chat.id), list):
                    PDF[message.chat.id] = []
                
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                
                try:
                    os.makedirs(f"./{message.chat.id}/imgs")
                
                except Exception:
                    pass
                
                with open(
                    f"./{message.chat.id}/imgs/{message.chat.id}{isPdfOrImg}", "wb"
                ) as new_file:
                    new_file.write(downloaded_file)
                
                img = Image.open(
                    f"./{message.chat.id}/imgs/{message.chat.id}{isPdfOrImg}"
                ).convert("RGB")
                
                PDF[message.chat.id].append(img)
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    text=f"""`Added {len(PDF[message.chat.id])} page/'s to your pdf..`

/generate to generate PDF""",
                    message_id=picMsgId.message_id,
                )
            
            except Exception as e:
                
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    text=f"""Something went wrong.Try again or contact @rizad_x96

`ERROR: {e}`
""",
                    message_id=picMsgId.message_id,
                )
                sleep(5)
                bot.delete_message(
                    chat_id=message.chat.id, message_id=picMsgId.message_id
                )
                bot.delete_message(
                    chat_id=message.chat.id, message_id=message.message_id
                )
        
        elif fileExt.lower() == ".pdf":
            
            try:
                bot.send_chat_action(message.chat.id, "typing")
                pdfMsgId = bot.reply_to(
                    message,
                    "`Downloading your pdf..`",
                )
                
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                
                os.mkdir(f"./{message.message_id}pdf{message.chat.id}")
                with open(
                    f"./{message.message_id}pdf{message.chat.id}/pdf.pdf", "wb"
                ) as new_file:
                    new_file.write(downloaded_file)
                
                doc = fitz.open(f"./{message.message_id}pdf{message.chat.id}/pdf.pdf")
                zoom = 1
                mat = fitz.Matrix(zoom, zoom)
                noOfPages = doc.pageCount
                percNo = 0

                bot.edit_message_text(
                    chat_id=message.chat.id,
                    text=f"`Total pages: {noOfPages}`",
                    message_id=pdfMsgId.message_id,
                )
                
                totalPgList = list(range(0, noOfPages))
                
                for i in range(0, noOfPages, 10):
                    pgList = totalPgList[i : i + 10]
                    os.mkdir(f"./{message.message_id}pdf{message.chat.id}/pgs")
                    
                    for pageNo in pgList:
                        page = doc.loadPage(pageNo)
                        pix = page.getPixmap(matrix=mat)
                        cnvrtpg = pageNo + 1
                        
                        bot.edit_message_text(
                            chat_id=message.chat.id,
                            text=f"`Converted: {cnvrtpg}/{noOfPages} pgs`",
                            message_id=pdfMsgId.message_id,
                        )
                        
                        with open(
                            f"./{message.message_id}pdf{message.chat.id}/pgs/{pageNo}.jpg",
                            "wb",
                        ) as f:
                            pix.writePNG(
                                f"./{message.message_id}pdf{message.chat.id}/pgs/{pageNo}.jpg"
                            )
                            
                    directory = f"./{message.message_id}pdf{message.chat.id}/pgs"
                    imag = [
                        os.path.join(directory, file) for file in os.listdir(directory)
                    ]
                    imag.sort(key=os.path.getctime)
                    
                    percNo = percNo + len(imag)
                    media[message.chat.id] = []
                    LrgFileNo = 0
                    percentage = (percNo * 100) / noOfPages
                    
                    bot.edit_message_text(
                        chat_id=message.chat.id,
                        text=f"`Uploaded : {percentage:.2f}%`",
                        message_id=pdfMsgId.message_id,
                    )
                    
                    for file in imag:
                        if os.path.getsize(file) >= 1000000:
                            
                            picture = Image.open(file)
                            CmpImg = f"./{message.message_id}pdf{message.chat.id}/pgs/temp{LrgFileNo}.jpeg"
                            picture.save(CmpImg, "JPEG", optimize=True, quality=50)
                            
                            LrgFileNo += 1
                            if os.path.getsize(CmpImg) >= 1000000:
                                continue
                            
                            else:
                                fi = open(CmpImg, "rb")
                                media[message.chat.id].append(InputMediaPhoto(fi))
                                continue
                            
                        fi = open(file, "rb")
                        media[message.chat.id].append(InputMediaPhoto(fi))
                        
                    shutil.rmtree(f"./{message.message_id}pdf{message.chat.id}/pgs")
                    sleep(3)
                    bot.send_chat_action(message.chat.id, "upload_photo")
                    bot.send_media_group(message.chat.id, media[message.chat.id])
                    del media[message.chat.id]
                
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    text="`Uploading Completed..`",
                    message_id=pdfMsgId.message_id,
                )
                
                shutil.rmtree(f"./{message.message_id}pdf{message.chat.id}")
                
                sleep(10)
                bot.send_chat_action(message.chat.id, "typing")
                feedbackMsg = """
[Creator](https://telegram.me/rizad_x96)
"""
                bot.send_message(
                    message.chat.id, feedbackMsg, disable_web_page_preview=True
                )
                
                os.remove(f"./{message.message_id}pdf{message.chat.id}/pdf.pdf")
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    text="`started Uploading.`",
                    message_id=pdfMsgId.message_id,
                )
                
            except Exception as e:
                
                try:
                    shutil.rmtree(f"./{message.message_id}pdf{message.chat.id}")
                    
                    bot.edit_message_text(
                        chat_id=message.chat.id,
                        text=f"""Something went wrong.Try again or contact @rizad_x96

`ERROR: {e}`
""",
                        message_id=pdfMsgId.message_id,
                    )
                    
                    sleep(15)
                    bot.delete_message(
                        chat_id=message.chat.id, message_id=pdfMsgId.message_id
                    )
                    bot.delete_message(
                        chat_id=message.chat.id, message_id=message.message_id
                    )
                except Exception:
                    pass

        elif fileExt.lower() in suprtedPdfFile:
            
            try:
                
                bot.send_chat_action(message.chat.id, "typing")
                pdfMsgId = bot.reply_to(
                    message,
                    "`Downloading your file.`",
                )
                
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                
                os.mkdir(f"./{message.message_id}pdf{message.chat.id}")
                with open(
                    f"./{message.message_id}pdf{message.chat.id}/{isPdfOrImg}", "wb"
                ) as new_file:
                    new_file.write(downloaded_file)
                
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    text="Creating pdf.",
                    message_id=pdfMsgId.message_id,
                )
                Document = fitz.open(
                    f"./{message.message_id}pdf{message.chat.id}/{isPdfOrImg}"
                )
                b = Document.convert_to_pdf()
                pdf = fitz.open("pdf", b)
                pdf.save(
                    f"./{message.message_id}pdf{message.chat.id}/{fileNm}.pdf",
                    garbage=4,
                    deflate=True,
                )
                pdf.close()
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    text="Started Uploading.",
                    message_id=pdfMsgId.message_id,
                )
                
                sendfile = open(
                    f"./{message.message_id}pdf{message.chat.id}/{fileNm}.pdf", "rb"
                )
                bot.send_document(
                    message.chat.id, sendfile, caption=f"` Converted: {fileExt} to pdf`"
                )
                bot.edit_message_text(
                    chat_id=message.chat.id,
                    text="Uploading Completed.",
                    message_id=pdfMsgId.message_id,
                )
                
                shutil.rmtree(f"./{message.message_id}pdf{message.chat.id}")
                
                sleep(10)
                bot.send_chat_action(message.chat.id, "typing")
                feedbackMsg = """
[Developer](https://telegram.me/rizad_x96)
"""
                bot.send_message(
                    message.chat.id, feedbackMsg, disable_web_page_preview=True
                )

            except Exception as e:
                
                try:
                    shutil.rmtree(f"./{message.message_id}pdf{message.chat.id}")
                    bot.edit_message_text(
                        chat_id=message.chat.id,
                        text=f"""Something went wrong.Try again or contact @rizad_x96

`ERROR: {e}`
""",
                        message_id=pdfMsgId.message_id,
                    )
                    
                    sleep(15)
                    bot.delete_message(
                        chat_id=message.chat.id, message_id=pdfMsgId.message_id
                    )
                    bot.delete_message(
                        chat_id=message.chat.id, message_id=message.message_id
                    )

                except Exception:
                    pass

        elif fileExt.lower() in suprtedPdfFile2:
            
            if os.getenv("CONVERT_API") is None:
                
                pdfMsgId = bot.reply_to(
                    message,
                    "`Forgot to add ConvertAPI.. Contact @rizad_x96`",
                )
                sleep(15)
                bot.delete_message(
                    chat_id=message.chat.id, message_id=pdfMsgId.message_id
                )
            
            else:
                
                try:
                    
                    bot.send_chat_action(message.chat.id, "typing")
                    pdfMsgId = bot.reply_to(
                        message,
                        "`Downloading your file.`",
                    )
                    
                    file_info = bot.get_file(message.document.file_id)
                    downloaded_file = bot.download_file(file_info.file_path)
                    
                    os.mkdir(f"./{message.message_id}pdf{message.chat.id}")
                    with open(
                        f"./{message.message_id}pdf{message.chat.id}/{isPdfOrImg}", "wb"
                    ) as new_file:
                        new_file.write(downloaded_file)
                    
                    bot.edit_message_text(
                        chat_id=message.chat.id,
                        text="Creating pdf.",
                        message_id=pdfMsgId.message_id,
                    )
                    convertapi.convert(
                        "pdf",
                        {
                            "File": f"./{message.message_id}pdf{message.chat.id}/{isPdfOrImg}"
                        },
                        from_format=fileExt[1:],
                    ).save_files(
                        f"./{message.message_id}pdf{message.chat.id}/{fileNm}.pdf"
                    )
                    bot.edit_message_text(
                        chat_id=message.chat.id,
                        text="Uploading Completed.",
                        message_id=pdfMsgId.message_id,
                    )
                    sendfile = open(
                        f"./{message.message_id}pdf{message.chat.id}/{fileNm}.pdf", "rb"
                    )
                    bot.send_document(
                        message.chat.id,
                        sendfile,
                        caption=f"` Converted: {fileExt} to pdf`",
                    )
                    
                    shutil.rmtree(f"./{message.message_id}pdf{message.chat.id}")
                    
                    sleep(10)
                    bot.send_chat_action(message.chat.id, "typing")
                    feedbackMsg = """
[Developer](https://telegram.me/rizad_x96)"""
                    bot.send_message(
                        message.chat.id, feedbackMsg, disable_web_page_preview=True
                    )
                    
                except Exception:
                    
                    try:
                        shutil.rmtree(f"./{message.message_id}pdf{message.chat.id}")
                        bot.edit_message_text(
                            chat_id=message.chat.id,
                            text="""ConvertAPI limit reaches.. contact Owner""",
                            message_id=pdfMsgId.message_id,
                        )
                        
                    except Exception:
                        pass
        
        else:
            
            try:
                bot.send_chat_action(message.chat.id, "typing")
                unSuprtd = bot.send_message(
                    message.chat.id, """`unsupported file.`"""
                )
                sleep(15)
                bot.delete_message(
                    chat_id=message.chat.id, message_id=message.message_id
                )
                bot.delete_message(
                    chat_id=message.chat.id, message_id=unSuprtd.message_id
                )
            except Exception:
                pass
            
    except Exception:
        pass


@bot.message_handler(commands=["cancel"])
def delQueue(message):

    try:
        bot.send_chat_action(message.chat.id, "typing")
        shutil.rmtree(f"./{message.chat.id}")
        bot.reply_to(message, "`Queue deleted Successfully..`")
        
        try:
            del PDF[message.chat.id]
        except Exception:
            pass

    except Exception:
        bot.reply_to(message, "`No Queue founded`")


@bot.message_handler(commands=["generate"])
def generate(message):
    try:
        bot.send_chat_action(message.chat.id, "typing")
        newName = message.text.replace("/generate", "")
        images = PDF.get(message.chat.id)
        
        if isinstance(images, list):
            pgnmbr = len(PDF[message.chat.id])
            del PDF[message.chat.id]
        
        if not images:
            ntFnded = bot.reply_to(message, "`No image founded.!!`")
            sleep(5)
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            bot.delete_message(chat_id=message.chat.id, message_id=ntFnded.message_id)
            return
        
        gnrtMsgId = bot.send_message(message.chat.id, f"`Generating pdf..`")
        
        if newName == " name":
            fileName = f"{message.from_user.first_name}" + ".pdf"
        
        elif len(newName) > 0 and len(newName) <= 10:
            fileName = f"{newName}" + ".pdf"
        
        elif len(newName) > 10:
            fileName = f"{message.from_user.first_name}" + ".pdf"
        
        else:
            fileName = f"{message.chat.id}" + ".pdf"
        
        path = os.path.join(f"./{message.chat.id}", fileName)
        images[0].save(path, save_all=True, append_images=images[1:])
        bot.edit_message_text(
            chat_id=message.chat.id,
            text="`Uploading pdf..`",
            message_id=gnrtMsgId.message_id,
        )
        bot.send_chat_action(message.chat.id, "upload_document")
        
        sendfile = open(path, "rb")
        bot.send_document(
            message.chat.id,
            sendfile,
            caption=f"file Name: `{fileName}`\n\n`Total pg's: {pgnmbr}`",
        )
        bot.edit_message_text(
            chat_id=message.chat.id,
            text="`Successfully Uploaded`",
            message_id=gnrtMsgId.message_id,
        )
        
        shutil.rmtree(f"./{message.chat.id}")
        
        sleep(10)
        bot.send_chat_action(message.chat.id, "typing")
        feedbackMsg = """
[Developer](https://telegram.me/rizad_x96)
"""
        bot.send_message(message.chat.id, feedbackMsg, disable_web_page_preview=True)
        
    except Exception:
        pass


@bot.message_handler(
    content_types=[
        "text",
        "audio",
        "sticker",
        "video",
        "video_note",
        "voice",
        "location",
        "contact",
    ]
)
def unSuprtd(message):

    try:
        bot.send_chat_action(message.chat.id, "typing")
        unSuprtd = bot.send_message(
            message.chat.id, "`unsupported file.. please send me an image..😬`"
        )
        sleep(5)
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        bot.delete_message(chat_id=message.chat.id, message_id=unSuprtd.message_id)

    except Exception:
        pass


bot.polling()
