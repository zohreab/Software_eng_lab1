# Software_eng_lab1

# مدیریت نسخ پروژه و یکپارچه‌سازی مستمر

---

## روال انجام آزمایش

پروژه‌ی انتخاب‌شده برای این آزمایش، یک ماشین حساب ساده با قابلیت اجرای 6 عملیات محاسباتی به زبان پایتون است. برای فرایند توسعه با استفاده از ابزار گیت، ابتدا یک برنچ develop ساخته می‌شود و برای هر operation یک برنچ جدید روی develop با فرمت feat/operation_name ساخته می‌شود که پس از کامیت کردن تغییرات مد نظر برنچ، با pull request با برنچ develop مرج می‌شود.


## ساخت مخزن گیت‌هاب
ابتدا یک مخزن گیت‌هاب برای آزمایش مذکور توسط یکی از اعضا ساخته‌شده و سپس عضو دیگر به عنوان collaborator به پروژه اضافه شد. در تنظیمات مخزن، برنچ main به عنوان پروتکتد لحاظ شد تا بدون pull request انجام تغییرات در main مجاز نباشد. همچنین همان‌طور که در شکل زیر مشخص است، تیک require pull requests باید فعال باشد:

![alt text](./images/require_pull_req.jpeg)



## اضافه کردن برنچ‌ها
ابتدا یک برنچ develop به پروژه اضافه شد تا روند توسعه در این برنچ و نه روی main انجام شود. سپس برای هر operation یک برنچ ساخته‌ شد و پس اضافه کردن بخش مورد نظر برنچ مذکور یک pull request برای مرج شدن با develop داد که owner مخزن پس از بررسی برنچ مد نظر اگر مشکلی وجود نداشت این درخواست را تایید می‌کرد. تصاویر زیر این مرحله را برای برنچ feat/root نشان می‌دهد:

![alt text](./images/pull_req_1.jpeg) ![alt text](./images/pull_req_2.jpeg) ![alt text](./images/pull_req_3.jpeg)![alt text](./images/pull_req_4.jpeg) ![alt text](./images/pull_req_5.jpeg)

## حل کردن conflictهای ایجاد‌شده
در طول فرایند مرج کردن برنچ‌ها دو conflict پس از pull request ایجاد شد که یکی به علت عقب بودن tip برنچ مد نظر از برنچ base و دیگری به سبب ایجاد تغییر اشتباهی توسط یکی از اعضا بر روی بخش مربوط به برنچ یکی دیگر از operationها بود. تصاویری از دو conflict ایجادشده و نحوه‌ی حل یکی از آن‌ها در قسمت زیر اضافه شده است:

![alt text](./images/conflict_1.jpeg) ![alt text](./images/conflict_2_1.jpeg) ![alt text](./images/conflict_2_2.jpeg) ![alt text](./images/conflict_2_3.jpeg) ![alt text](./images/conflict_2_4.jpeg) ![alt text](./images/conflict_2_5.jpeg) ![alt text](./images/conflict_2_6.jpeg)

## پرسش‌ها

علاوه بر گزارش آزمایش، پاسخ سوالات زیر را هم داخل فایل README بنویسید:

1. پوشه‌ی .git چیست؟ چه اطلاعاتی در آن ذخیره می‌شود؟ با چه دستوری ساخته می‌شود؟

پوشه‌ی .git یک پوشه‌ی مخفی است که به طور خودکار هنگامی که یک مخزن Git را در یک پوشه با استفاده از دستور "git init" می‌سازیم، ایجاد می‌شود. این پوشه شامل تمام اطلاعات مورد نیاز برای کنترل نسخه (version control) است. برای مثال اگر بخواهیم مخزن خود را کلون کنیم، کافیست git. را کپی کنیم. این پوشه همچنین حاوی یک log است که تاریخچه‌ی commitها را ذخیره می‌کند. این log می‌تواند به ما کمک کند تا به نسخه‌ی مورد نظر از کدمان بازگردیم.
   
برخی زیرپوشه‌ها و فایل‌هایی که در این پوشه یافت می‌شوند عبارتند از:    
   
   پوشه‌ی hooks: این پوشه حاوی فایل‌های اسکریپت است. Git hookها اسکریپت‌هایی هستند که قبل یا بعد از رویدادهایی مانند commit، push و غیره اجرا می‌شوند.    
   
   پوشه‌ی اشیاء: این پوشه یک پایگاه داده شی از Git را نشان می‌دهد.    
   
   فایل config: این فایل پیکربندی محلی است.    
   
   پوشه‌ی refs: این پوشه اطلاعات مربوط به برچسب‌ها و شاخه‌ها را ذخیره می‌کند.   
   
   فایل HEAD: این فایل ارجاعی به شاخه فعلی را ذخیره می‌کند. به طور پیش‌فرض به شاخه اصلی اشاره می‌کند.    
   
   فایل index: یک فایل باینری است و اطلاعات مرحله‌بندی را ذخیره می‌کند.
   
همان‌طور که گفته‌شد، این پوشه با دستور git init در آن پوشه‌ای که این دستور وارد شده، ساخته می‌شود.

---

2. منظور از atomic بودن در atomic commit و atomic pull-request چیست؟
  
  در Git، منظور از atomic commit یک commit واحد است که شامل مجموعه‌ای از تغییرات است که از نظر منطقی مرتبط هستند و باید با هم اعمال شوند. atomic commit اغلب برای گروه‌بندی تغییراتی که مربوط به یک ویژگی خاص یا رفع اشکال هستند استفاده می‌شود و درک هدف و زمینه تغییرات را آسان‌تر می‌کند.
  کار با atomic commit به این معنی است که commitهای شما کوچک‌ترین اندازه ممکن را دارند. هر commit یک و فقط یک کار ساده انجام می‌دهد که می تواند در یک جمله‌ی ساده خلاصه شود. مقدار تغییر کد مهم نیست. می تواند یک حرف یا صد هزار خط باشد، اما شما باید بتوانید تغییر را با یک جمله کوتاه ساده توصیف کنید.

  این موضوع برای atomic pull request هم صادق است. یعنی باید شامل مجموعه‌ای از تغییرات باشد که از نظر منطقی مرتبط هستند و باید با هم اعمال شوند. اغلب برای گروه‌بندی تغییرات مربوط به یک feature خاص یا رفع یک bug استفاده می شود. بنابراین برای pull requestها هم مهم است که اتمی باشند. اما در یک atomic pull request، ما موفقیت در اتمی بودن را به عنوان توانایی در ارائه کوچکترین عملکرد ممکن اندازه‌گیری می‌کنیم، که می‌تواند از یک یا چند atomic commit تشکیل شده باشد.
  
---

3. تفاوت دستورهای fetch و pull و merge و rebase را بیان کنید.

در Git، دستورات اصلی برای این که بتوانیم با مخازن remote تعامل داشته باشیم و تغییرات را در مخزن محلی خود ادغام کنیم، fetch، pull، merge و rebase هستند. 

دستور Fetch: دستور "git fetch" تغییرات را از یک مخزن راه دور بازیابی می کند و آنها را در مخزن محلی شما ذخیره می کند. این تغییرات را در شعبه محلی شما ادغام نمی کند، بلکه دانش مخزن محلی شما را از شعبه راه دور به روز می کند.

دستور Pull: دستور "git pull" تغییرات را از یک مخزن راه دور واکشی می کند و آنها را در شعبه محلی شما ادغام می کند. اساساً ترکیبی از "git fetch" و "git merge" است. در صورت وجود هرگونه تضاد بین شعب محلی و راه دور، باید آنها را به صورت دستی حل کنید.

دستور Merge: دستور "git merge" دو یا چند شاخه را در یک شاخه ترکیب می کند. برای ادغام تغییرات از یک شاخه به شاخه دیگر استفاده می شود. هنگامی که دو شاخه را ادغام می کنید، Git یک commit جدید ایجاد می کند که تغییرات هر دو شاخه را ترکیب می کند.

دستور Rebase: دستور "git rebase" شبیه به "git merge" است که تغییرات را از یک شاخه به شاخه دیگر ترکیب می کند. با این حال، به جای ایجاد یک commit جدید برای ادغام تغییرات، "git rebase" تاریخچه commit شاخه هدف را با اعمال تغییرات از شاخه منبع بر روی commit های شاخه هدف یک به یک بازنویسی می کند. این منجر به یک تاریخچه ارتکاب خطی و تمیزتر می شود.

بنابراین به طور خلاصه، fetch دانش مخزن محلی ما را از شاخه‌ی remote به روز می‌کند، pull تغییرات را از یک مخزن remote واکشی می‌کند و آن‌ها را در نسخه‌ی محلی ما ادغام می‌کند، merge دو شاخه را در یک شاخه واحد ترکیب می‌کند و rebase تاریخچه‌ی commitهای شاخه هدف را برای اعمال تغییرات از شاخه منبع بازنویسی می‌کند. 

---
4. تفاوت چهار دستور reset و revert و restore را بیان کنید.

در Git، دستورات اصلی که به ما این امکان را می‌دهند تا تغییرات ایجاد شده در مخزن خود را لغو کنیم عبارتند از reset، revert و restore.

دستور Reset: دستور reset به ما این امکان را می‌دهد که وضعیت مخزن خود را به یک commit قبلی بازنشانی کنیم. این دستور نشانگر HEAD و نشانگر شاخه فعلی را به یک commit دیگر منتقل می‌کند و تغییرات ایجادشده پس از آن commit را کنار می‌گذارد. می توان از آن برای لغو یک commit و کنار گذاشتن تغییرات استفاده کرد.

دستور Revert: دستور revert یک commit جدید ایجاد می‌کند که تغییرات ایجادشده در commit قبلی را لغو می‌کند. این دستور تاریخچه مخزن ما را تغییر نمی‌دهد، بلکه یک commit جدید اضافه می‌کند که به طور موثر تغییرات ایجادشده در commit قبلی را لغو می‌کند. این دستور می‌تواند برای وقتی که به لغو یک commit  که قبلاً به یک مخزن remote منتقل شده‌است نیاز داریم، مفید باشد.

دستور Restore: دستور restore به ما اجازه می‌دهد تا فایل‌های موجود در فهرست کاری خود را به حالت قبلی بازگردانیم. از این دستور می‌توان برای لغو تغییرات فایل‌هایی که هنوز انجام نشده‌اند استفاده کرد. 

به طور خلاصه، reset به ما اجازه می‌دهد تا وضعیت مخزن خود را به یک commit قبلی بازنشانی کنیم، revert یک commit جدید ایجاد می‌کند که تغییرات ایجاد‌شده در commit قبلی را خنثی می‌کند، restore به ما این امکان را می‌دهد که فایل‌ها را در مخزن خود بازیابی کنیم. پوشه کار به حالت قبلی می رسد.

---
5. منظور از stage چیست؟ دستور stash چه کاری را انجام می‌دهد؟

در Git، منظور از stage، فرآیند آماده‌سازی تغییرات برای commit شدن در مخزن است. هنگامی که در فایل‌های پوشه‌ی خود تغییراتی ایجاد می کنیم، می توان از دستور add برای stage کردن آن تغییرات استفاده کنیم. stage کردن تغییرات به این معنی است که ما آن‌ها را به قسمت stage اضافه می‌کنیم، که یک منطقه‌ی ذخیره‌سازی موقت است که تغییراتی را در خود جای می‌دهد که آماده‌ی commit شدن هستند.
پس از stage شدن تغییرات، می‌توان از دستور commit برای ارسال این تغییرات به مخزن استفاده کنیم. هنگامی که تغییرات را commit می‌کنیم، Git یک snapshot جدید از مخزن ایجاد می‌کند که شامل تغییراتی است که stage کرده‌بودیم.

دستور stash در Git به ما این امکان را می‌دهد که تغییراتی را که هنوز آماده‌ی commit نیستند، به طور موقت ذخیره کنیم. هنگامی که دستور stash را اجرا می کنیم، Git تغییراتمان را در یک فضای ذخیره‌سازی موقت به نام stash ذخیره می‌کند. stash به ما اجازه می‌دهد بدون commit تغییرات خود به شاخه‌ی دیگری برویم یا روی بخش دیگری کار کنیم.
بعداً، هنگامی که آماده ادامه کار بر روی تغییرات stashشده بودیم، می‌توان از دستور stash application برای اعمال تغییرات در پوشه‌ی خود استفاده کنیم. این دستور، تغییراتی را که stash کرده‌بودیم را بازیابی می‌کند و به ما اجازه می‌دهد روی آن‌ها کار کنیم.
دستور stash زمانی مفید است که باید به کار یا شاخه‌ی دیگری تغییر مکان دهیم اما نمی خواهیم تغییرات ناقصی را در مخزن خود commit کنیم.

---
6. مفهوم snapshot به چه معناست؟

مفهوم snapshot به وضعیت یک مخزن در یک نقطه‌ی خاص از زمان اشاره دارد. هنگامی که یک commit در Git ایجاد می‌کنیم، Git یک snapshot از کل مخزن در آن نقطه از زمان می‌گیرد. این snapshot شامل محتویات تمام فایل‌های موجود در مخزن و همچنین ابرداده‌های مرتبط با آن فایل‌ها، مانند پیام commit، نویسنده و برچسب زمانی است.
هر commit در Git نمایانگر یک snapshot منحصر به فرد از مخزن در یک زمان خاص است که به این معناست که ما می توانیم به عقب برگردیم و با بررسی یک commit خاص، وضعیت مخزن را در هر نقطه از گذشته مشاهده کنیم. همچنین می‌توان تغییرات بین snapshotهای مختلف را مقایسه کرد تا ببینیم که مخزن در طول زمان چگونه تکامل یافته‌است.
برای کنترل نسخه در Git، وجود snapshot حیاتیست. با گرفتن snapshotها از مخزن در هر commit، این امکان فراهم می‌شود تا تغییرات کد خود را دنبال کنیم و با دیگران در یک پایگاه کد مشترک همکاری کنیم. 
